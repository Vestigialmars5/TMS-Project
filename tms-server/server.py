from flask import Flask, jsonify, request
from flask_cors import CORS
import osmnx as ox
import matplotlib.pyplot as plt
import networkx as nx
import json
from math import dist
from shapely.geometry import LineString


app = Flask(__name__)
CORS(app)

TEST_GRAPH = (
    "C:/Users/Milo/OneDrive/Escritorio/ROAD/Portfolio/tms/tests/test-graph.graphml"
)


# Returns the list of coordinates
@app.route("/api-test", methods=["GET", "POST"])
def api_coordinates():
    if request.method == "POST":
        try:
            # Extract data from request
            data = request.get_json()
            origin_coordinates = [data.get("originLat"), data.get("originLng")]
            destination_coordinates = [
                data.get("destinationLat"),
                data.get("destinationLng"),
            ]

            # Loads graph and retrieves the edges data
            graph = load_multidigraph(TEST_GRAPH)

            # Closest node to the coordinate inputed
            origin_id = get_closest_node(
                graph, origin_coordinates[1], origin_coordinates[0]
            )
            destination_id = get_closest_node(
                graph, destination_coordinates[1], destination_coordinates[0]
            )

            coordinates = calculate_route_coordinates(
                graph,
                origin_id,
                destination_id,
                origin_coordinates,
                destination_coordinates,
            )

            return jsonify(coordinates)
        except Exception as e:
            result = {"status": "error", "message": str(e)}
            return jsonify(result)
    else:
        return {}


# Calculates the coordinates along the route including pre and post
def calculate_route_coordinates(
    graph,
    origin_id,
    destination_id,
    origin_coordinates,
    destination_coordinates,
):
    # Extract nodes data for finding specific node coordinates
    nodes_data = ox.graph_to_gdfs(graph, nodes=True, edges=False)

    # Extract edges data for finding specific edges
    edges_data = ox.graph_to_gdfs(graph, nodes=False, edges=True)
    edges_data = edges_data.sort_index(level=["u", "v"])

    # Get coordinates and new origin_coordinates node to get precise starting location
    starting_option1, starting_option2 = get_segment_to_starting_node(
        graph, nodes_data, edges_data, origin_coordinates, origin_id
    )

    new_origin_id = starting_option1[1]

    print("starting finishing options")
    # Get coordinates and new origin_coordinates node to get precise finishing location
    finishing_option1, finishing_option2 = get_segment_to_finishing_node(
        graph, edges_data, destination_coordinates, destination_id
    )

    new_destination_id = finishing_option1[1]

    # Calculate the route from the new origin to the new destination
    route = get_shortest_route(graph, new_origin_id, new_destination_id)

    pre_coordinates = starting_option1[0]
    post_coordinates = finishing_option1[0]

    if starting_option2:
        # Check if second node is the second starting option
        if len(route) > 1 and route[1] == starting_option2[1]:
            # Makes starting node option2 start
            route.pop(0)
            pre_coordinates = starting_option2[0]

    if finishing_option2:
        # Check if second to last node is the second finishing option
        if (len(route) - 1 > 0) and (route[-1] == finishing_option2[1]):
            # Makes finishing node finishing_option2 finish
            route.pop()
            post_coordinates = finishing_option2[0]
    print("route", route, "\n")

    route_info = get_route_info_per_road(edges_data, route, coordinates=True)

    # Extract coordinates into usable list
    coordinates = []
    for road in route_info:
        coordinates += list(road["coordinates"].coords)

    print("pre coords", pre_coordinates)
    print()
    print(coordinates)
    print()
    print("post coords", post_coordinates)

    return merge_lists(pre_coordinates, coordinates, post_coordinates)


# Decides what will be the starting node for the route, checking if edge exists
# Also checks for the case where the closest node doesn't form part of the closest edge, in this case the edge takes priority
# Returns a list of tuples, (pre_start, starting_node) and the inverse if the road is two-ways else an empty tuple
def decide_starting_node_and_edge(
    nodes_data, edges_data, found_edge, closest_node, origin_coordinates
):
    closest_usable_node = closest_node

    # Node not part of the closest edge
    if closest_usable_node != found_edge[0] and closest_usable_node != found_edge[1]:
        # Get both coordinates
        node1_coords = nodes_data.loc[found_edge[0], ["y", "x"]]
        node1_x = node1_coords.at["x"]
        node1_y = node1_coords.at["y"]

        node2_coords = nodes_data.loc[found_edge[1], ["y", "x"]]
        node2_x = node2_coords.at["x"]
        node2_y = node2_coords.at["y"]

        origin_x = origin_coordinates[1]
        origin_y = origin_coordinates[0]

        node1_distance = dist([origin_x, origin_y], [node1_x, node1_y])
        node2_distance = dist([origin_x, origin_y], [node2_x, node2_y])

        closest_usable_node = (
            found_edge[0] if node1_distance < node2_distance else found_edge[1]
        )

    if edges_data.loc[(found_edge[0], found_edge[1]), "oneway"].item():
        # One way street
        return [(found_edge[0], found_edge[1]), ()]

    else:
        # Two way
        furthest_node = (
            found_edge[0] if found_edge[1] == closest_usable_node else found_edge[1]
        )

        return [
            (furthest_node, closest_usable_node),
            (closest_usable_node, furthest_node),
        ]


# Merges the list of coordinates
def merge_lists(pre, coordinates, post):
    """n = len(pre)
    missing = []
    index = 0
    for i in range(n):
        if pre[i] not in coordinates:
            missing.append(pre[i])
        else:
            index = coordinates.index(pre[i])
            break

    merged = missing + coordinates[index:]"""
    print("here", pre, post, "hi")
    n = len(post)
    for i in range(n):
        if post[i] in pre:
            return post[i:]

    return pre + coordinates + post


# Gets the segment bewteen the closest point in the coordinate on the edge to the node
def get_segment_to_starting_node(
    graph, nodes_data, edges_data, origin_coordinates, origin_id
):
    found_edge = ox.distance.nearest_edges(
        graph, origin_coordinates[1], origin_coordinates[0]
    )

    # Find the options for pre and start, in case the node is in the route change start with pre
    decided_nodes = decide_starting_node_and_edge(
        nodes_data, edges_data, found_edge, origin_id, origin_coordinates
    )
    option1 = decided_nodes[0]
    option2 = decided_nodes[1]

    # Get interpolation for option 1
    pre_route_info_option1 = get_route_info_per_road(
        edges_data, [option1[0], option1[1]], coordinates=True
    )

    interpolated1 = ox.utils_geo.interpolate_points(
        pre_route_info_option1[0]["coordinates"], 0.0001
    )

    interpolated1 = list(interpolated1)

    starting_index1 = get_closest_coordinate_index(
        interpolated1, origin_coordinates[1], origin_coordinates[0]
    )

    path_option1 = (
        find_path_from_edge_to_origin(interpolated1, starting_index1),
        option1[1],
    )

    # If option2 exists get interpolation
    if option2:
        pre_route_info_option2 = get_route_info_per_road(
            edges_data, [option2[0], option2[1]], coordinates=True
        )

        interpolated2 = ox.utils_geo.interpolate_points(
            pre_route_info_option2[0]["coordinates"], 0.0001
        )

        interpolated2 = list(interpolated2)

        starting_index2 = get_closest_coordinate_index(
            interpolated2, origin_coordinates[1], origin_coordinates[0]
        )

        path_option2 = (
            find_path_from_edge_to_origin(interpolated2, starting_index2),
            option2[1],
        )
    else:
        path_option2 = []
    return (path_option1, path_option2)


# Gets the segment bewteen the closest point in the coordinate on the edge to the node
def get_segment_to_finishing_node(
    graph, edges_data, destination_coordinates, destination_id
):
    found_edge = ox.distance.nearest_edges(
        graph, destination_coordinates[1], destination_coordinates[0]
    )
    print("found edge", found_edge)
    print("closest edge", destination_id)

    # Find the options for post and start, in case the node is in the route change start with post
    decided_nodes = decide_finishing_node_and_edge(
        edges_data, found_edge, destination_id
    )

    option1 = decided_nodes[0]
    option2 = decided_nodes[1]

    # Get interpolation for option 1
    post_route_info_option1 = get_route_info_per_road(
        edges_data, [option1[0], option1[1]], coordinates=True
    )

    interpolated1 = ox.utils_geo.interpolate_points(
        post_route_info_option1[0]["coordinates"], 0.0001
    )

    interpolated1 = list(interpolated1)

    finishing_index1 = get_closest_coordinate_index(
        interpolated1, destination_coordinates[1], destination_coordinates[0]
    )

    path_option1 = (
        find_path_from_destination_to_edge(interpolated1, finishing_index1),
        option1[0],
    )

    # If option2 exists get interpolation
    if option2:
        post_route_info_option2 = get_route_info_per_road(
            edges_data, [option2[0], option2[1]], coordinates=True
        )

        interpolated2 = ox.utils_geo.interpolate_points(
            post_route_info_option2[0]["coordinates"], 0.0001
        )

        interpolated2 = list(interpolated2)

        finishing_index2 = get_closest_coordinate_index(
            interpolated2, destination_coordinates[1], destination_coordinates[0]
        )

        path_option2 = (
            find_path_from_destination_to_edge(interpolated2, finishing_index2),
            option2[1],
        )
    else:
        path_option2 = []
    print("options", path_option1)
    print("options", path_option2)
    print()
    return (path_option1, path_option2)


# Decides what will be the finishing node for the route, checking if edge exists
# Returns a list of tuples, (post_finish, finishing_node) and the inverse if the road is two-ways else an empty tuple
def decide_finishing_node_and_edge(edges_data, found_edge, closest_node):
    if edges_data.loc[(found_edge[0], found_edge[1]), "oneway"].item():
        # One way street
        return [(found_edge[0], found_edge[1]), ()]

    else:
        # Two way
        furthest_node = (
            found_edge[0] if found_edge[1] == closest_node else found_edge[1]
        )

        return [(furthest_node, closest_node), (closest_node, furthest_node)]


def get_closest_coordinate_index(coordinates, x, y):
    closest = {"index": 0, "distance": float("inf")}

    for i in range(len(coordinates)):
        xy_points = [point for point in coordinates[i]]
        curr_dist = dist(xy_points, [y, x])
        if curr_dist < closest["distance"]:
            closest["index"] = i
            closest["distance"] = curr_dist

    return closest["index"]


def find_path_from_edge_to_origin(linestring, starting_index):
    coords = []
    for i in range(starting_index, len(linestring)):
        coords.append(linestring[i])
    return coords


def find_path_from_destination_to_edge(linestring, finishing_index):
    coords = []
    for i in range(finishing_index + 1):
        coords.append(linestring[i])
    return coords


def get_closest_node(graph, x, y):
    return ox.distance.nearest_nodes(graph, x, y)


def read_graphml_file_content():
    # Open the .graphml file and read its content
    file_path = (
        "C:/Users/Milo/OneDrive/Escritorio/ROAD/Portfolio/tms/tms-server/data.json"
    )
    with open(file_path) as file:
        graph_content = json.load(file)
    return jsonify(graph_content)


def load_multidigraph(filepath):
    # Load a graph (replace with your graph file or creation method)
    graph = ox.load_graphml(filepath=filepath)
    graph = ox.add_edge_speeds(graph)
    return ox.speed.add_edge_travel_times(graph)


# Returns list of node IDs
def select_origin_destination(graph):
    # Plot the graph
    ox.plot_graph(graph, node_color="blue", node_size=10, show=False, close=False)

    # Allow the user to interactively click on two nodes
    selected_nodes = plt.ginput(2, timeout=0)

    if not selected_nodes:
        return None

    # Convert clicked coordinates to nearest nodes
    selected_node_ids = [
        ox.distance.nearest_nodes(graph, x, y) for x, y in selected_nodes
    ]

    # Close the plot
    plt.close()

    return selected_node_ids


# Returns route's nodes information as a list
def get_shortest_route(graph, origin_node_id, destination_node_id):
    return ox.shortest_path(graph, origin_node_id, destination_node_id)


# Returns a list of dictionaries
def get_route_info_per_road(
    edges_data, route, coordinates=False, highway=False, maxspeed=False, length=False
):
    if not coordinates and not highway and not maxspeed and not length:
        return []

    route_info = []
    for i in range(len(route) - 1):
        road_info = {}

        if coordinates:
            road_info["coordinates"] = get_edge_coordinates(
                edges_data, route[i], route[i + 1]
            )

        if highway:
            road_info["highway"] = get_edge_highway(edges_data, route[i], route[i + 1])

        if maxspeed:
            road_info["maxspeed"] = get_edge_maxspeed(
                edges_data, route[i], route[i + 1]
            )

        if length:
            road_info["length"] = get_edge_length(edges_data, route[i], route[i + 1])
        route_info.append(road_info)

    return route_info


# To get the exact coordinates that make an edge
def get_edge_coordinates(edges_data, node1, node2):
    print("inside", node1, node2)
    edge_geometry = edges_data.loc[(node1, node2), "geometry"]
    print("done")
    linestring = edge_geometry.iloc[0]
    linestring_list = list(linestring.coords)
    sorted_lat_long = [(lat, long) for long, lat in linestring_list]
    return LineString(sorted_lat_long)


def get_edge_highway(edges_data, node1, node2):
    edge_highway = edges_data.loc[(node1, node2), "highway"]
    result = edge_highway.iloc[0]
    return result


def get_edge_maxspeed(edges_data, node1, node2):
    edge_maxspeed = edges_data.loc[(node1, node2), "maxspeed"]
    result = edge_maxspeed.iloc[0]
    return result


def get_edge_length(edges_data, node1, node2):
    edge_length = edges_data.loc[(node1, node2), "length"]
    result = edge_length.iloc[0]
    return result


def dijkstra_algorithm(graph, origin, destination):
    # Makes sure I'm working with a multidigraph
    if not isinstance(graph, nx.MultiDiGraph):
        return ValueError("not multidigraph")

    # Create a dicitonary of the distances from origin
    distances = {node: float("inf") for node in graph.nodes}
    distances[origin] = 0

    # Create a dicitonary of the maxspeed from origin
    travel_time = {node: float("inf") for node in graph.nodes}
    travel_time[origin] = 0

    # Create a dictionary for the queue to keep track of the distances
    priority_queue_distances = {node: float("inf") for node in graph.nodes}
    priority_queue_distances[origin] = 0

    # Create a dictionary for the queue to keep track of the travel_times
    priority_queue_travel_time = {node: float("inf") for node in graph.nodes}
    priority_queue_travel_time[origin] = 0

    # To recunstruct the path later
    parents_distances = {node: None for node in graph.nodes}
    parents_travel_time = {node: None for node in graph.nodes}

    while priority_queue_distances:
        # Get the node with the minimum distance, and remove it from queue
        current_node = min(priority_queue_distances, key=priority_queue_distances.get)
        del priority_queue_distances[current_node]

        for neighbor, edge_data in graph[current_node].items():
            estimated_distance = distances[current_node] + edge_data[0]["length"]
            if estimated_distance < distances[neighbor]:
                distances[neighbor] = estimated_distance
                priority_queue_distances[neighbor] = estimated_distance
                parents_distances[neighbor] = current_node

    length_path = []
    current = destination
    while current is not None:
        length_path.insert(0, current)
        current = parents_distances[current]

    while priority_queue_travel_time:
        # Get the node with the minimum travel time
        current_node = min(
            priority_queue_travel_time, key=priority_queue_travel_time.get
        )
        del priority_queue_travel_time[current_node]

        for neighbor, edge_data in graph[current_node].items():
            estimated_travel_time = (
                travel_time[current_node] + edge_data[0]["travel_time"]
            )

            if estimated_travel_time < travel_time[neighbor]:
                travel_time[neighbor] = estimated_travel_time
                priority_queue_travel_time[neighbor] = estimated_travel_time
                parents_travel_time[neighbor] = current_node

    speed_path = []
    current = destination
    while current is not None:
        speed_path.insert(0, current)
        current = parents_travel_time[current]

    return (length_path, speed_path)


def main_runner():
    graph = load_multidigraph("./point_graph.graphml")
    origin, destination = select_origin_destination(graph)
    if origin is None or destination is None:
        print("here")
        return
    print(dijkstra_algorithm(graph, origin, destination))
    route = get_shortest_route(graph, origin, destination)
    route_info = get_route_info_per_road(graph, route)


if __name__ == "__main__":
    app.run(debug=True)

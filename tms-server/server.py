from flask import Flask, jsonify, request
from flask_cors import CORS
import osmnx as ox
import matplotlib.pyplot as plt
import networkx as nx
import json
from math import dist
from shapely.geometry import LineString, Point
import geopy.distance


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


def calculate_route_coordinates(
    graph,
    origin_id,
    destination_id,
    origin_coordinates,
    destination_coordinates,
):
    # Get coordinates for starting point
    # Get coordinates for finishing point
    # Check the direction of the street for the beginning and the end
    # If they are the same direction they might be in the same edge, check
    # Oneway (both) a->b
    # Only one direction to follow
    # Are they in the same edge?

    # If they are in the same edge if its the same direction a->b a->b
    # If the origin is closer to the oposite of the direction we can go without a route
    # Interpolate the edge get closest to starting coord and closest to finishing coord
    # start at the closest to start, finish at closest to finish
    #                       DONE

    # If the origin is not the oposite of the direction we need the route
    # Interpolate the edge to get the closest to the starting point and keep from there to the next node

    # If they arent in the same edge a->b ?->?
    # Make the oposite from the direction the first point and the following node the target (a->b) a would be the first
    # Interpolate the edge get closest to starting coord
    # start at the closest to start, finish at the end

    # If the origin is not the oposite of the direction we need the route
    # Interpolate the edge to get the closest to the starting point and keep from there to the next node

    # Twoways (both) a<->b
    # Can go either way
    # Are they in the same edge?

    # Extract nodes data for finding specific node coordinates
    nodes_data = ox.graph_to_gdfs(graph, nodes=True, edges=False)

    # Extract edges data for finding specific edges
    edges_data = ox.graph_to_gdfs(graph, nodes=False, edges=True)
    edges_data = edges_data.sort_index(level=["u", "v"])

    starting_edge_direction, finishing_edge_direction = get_direction_of_edges(
        graph,
        nodes_data,
        edges_data,
        origin_coordinates,
        origin_id,
        destination_coordinates,
        destination_id,
    )

    # Get coordinates and new origin_coordinates node to get precise starting location
    starting_option1, starting_option2 = get_segment_to_starting_node(
        graph, nodes_data, edges_data, origin_coordinates, origin_id
    )

    new_origin_id = starting_option1[1]
    print("new origin", new_origin_id)

    # Get coordinates and new origin_coordinates node to get precise finishing location
    finishing_option1, finishing_option2 = get_segment_to_finishing_node(
        graph, edges_data, destination_coordinates, destination_id
    )

    new_destination_id = finishing_option1[1]
    print("new destination", new_destination_id)

    if new_origin_id == new_destination_id:
        new_destination_id = finishing_option2[1]
        print("new stuff", new_destination_id)
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
            print("did something to pre, pre coords", pre_coordinates)

    if finishing_option2:
        # Check if second to last node is the second finishing option
        if (len(route) - 1 > 0) and (route[-1] == finishing_option2[1]):
            # Makes finishing node finishing_option2 finish
            route.pop()
            post_coordinates = finishing_option2[0]
            print("did something to post, post coordinates", post_coordinates)
    print("route", route, "\n")

    route_info = get_route_info_per_road(edges_data, route, coordinates=True)

    # Extract coordinates into usable list
    coordinates = []
    for road in route_info:
        coordinates += list(road["coordinates"].coords)

    return merge_lists(pre_coordinates, coordinates, post_coordinates)


# To plot a route we need to have a pre_route, route and post route
# To have a pre_route and post_route we need to get the direction of the


# Function to get a full route of coordinates returns list of coordinates
def get_full_route(
    graph,
    nodes_data,
    edges_data,
    origin_coordinates,
    closest_node_to_origin,
    destination_coordinates,
    closest_node_to_destination,
):
    # Get the nearest edge to the coordinate
    closest_edge_to_origin = ox.distance.nearest_edges(
        graph, origin_coordinates[1], origin_coordinates[0]
    )
    closest_edge_to_destination = ox.distance.nearest_edges(
        graph, destination_coordinates[1], destination_coordinates[0]
    )

    # Get usable nodes
    closest_node_to_origin = get_usable_node(
        nodes_data, closest_node_to_origin, closest_edge_to_origin
    )
    closest_node_to_destination = get_usable_node(
        nodes_data, closest_node_to_destination, closest_edge_to_destination
    )

    # Get the direction of the edges
    starting_edge_direction, finishing_edge_direction = get_direction_of_edges(
        edges_data, closest_edge_to_origin, closest_edge_to_destination
    )

    # If directions are same check if same edge
    if starting_edge_direction == finishing_edge_direction:
        if is_same_edge(
            starting_edge_direction, closest_edge_to_origin, closest_edge_to_destination
        ):
            # Same edge, changing name to found edge for clearer reading
            found_edge = closest_edge_to_origin

            # Get coordinates for the starting node
            target_node_coordinates = get_node_coordinates(nodes_data, found_edge[0])

            # Get distance from starting node to the origin or destination
            origin_distance_to_starting_node = get_distance_to_node(
                nodes_data, origin_coordinates, target_node_coordinates
            )
            destination_distance_to_starting_node = get_distance_to_node(
                nodes_data, destination_coordinates, target_node_coordinates
            )

            # Oneway
            if starting_edge_direction:
                if is_direct(
                    origin_distance_to_starting_node,
                    destination_distance_to_starting_node,
                ):
                    return get_pre_and_post(
                        edges_data,
                        found_edge,
                        origin_distance_to_starting_node,
                        destination_distance_to_starting_node,
                    )

            # Twoway
            else:
                if not is_direct(
                    origin_distance_to_starting_node,
                    destination_distance_to_starting_node,
                ):
                    # If it's not direct we can just inverse the found edge and we would get a direct edge
                    direct_edge = (found_edge[1], found_edge[0])

                    # Calculate previous coordinates and distance to new edge
                    target_node_coordinates = get_node_coordinates(
                        nodes_data, direct_edge[0]
                    )
                    origin_distance_to_starting_node = get_distance_to_node(
                        origin_coordinates, target_node_coordinates
                    )
                    destination_distance_to_starting_node = get_distance_to_node(
                        destination_coordinates, target_node_coordinates
                    )

                # Found edge is direct
                else:
                    direct_edge = found_edge

                return get_pre_and_post(
                    edges_data,
                    direct_edge,
                    origin_coordinates,
                    destination_coordinates,
                )

    # 2 cases left, one where route is needed and one where no route is needed because there is only 2 edges in total (a--->b--->c)


# Function to calculate a distance from a coordinate to the coordinates of a target node, returns a float distance
def get_distance_to_node(node_coordinates, target_node_coordinates):
    return dist(
        [node_coordinates[1], node_coordinates[0]],
        [target_node_coordinates[0], target_node_coordinates[1]],
    )


# Function to determine if a origin to destination is o->d and not o<-d, returns bool
def is_direct(distance_to_origin, distance_to_destination):
    if distance_to_origin <= distance_to_destination:
        # If origin is closer to starting node returns true
        return True

    # Destination is closer to starting point o<-d
    return False


# For direct case where we dont need a route, returns list of coordinates
def get_pre_and_post(edges_data, edge, origin_coordinates, destination_coordinates):
    # Get interpolation
    road_coordinates = get_route_info_per_road(
        edges_data, [edge[0], edge[1]], coordinates=True
    )
    interpolated = ox.utils_geo.interpolate_points(
        road_coordinates[0]["coordinates"], 0.00001
    )
    interpolated = list(interpolated)

    # Get closest index for origin and destination
    closest_index_origin = get_closest_coordinate_index(
        interpolated, origin_coordinates[1], origin_coordinates[0]
    )
    closest_index_destination = get_closest_coordinate_index(
        interpolated, destination_coordinates[1], destination_coordinates[0]
    )

    pre_post = get_coordinates_pre_post(
        interpolated, closest_index_origin, closest_index_destination
    )

    return pre_post

# Get coordinates between a start and a finish, returns a list of coords
def get_coordinates_pre_post(linestring, starting_index, finishing_index):
    coords = []
    for i in range(starting_index, finishing_index + 1):
        coords.append(linestring[i])
    return coords


# Check if node forms part of the closest edge, if not assign a node of the found edge as the new closest node. Returns node id
def get_usable_node(nodes_data, closest_node, closest_edge, coordinates):
    if not is_node_in_edge(closest_node, closest_edge):
        return assign_usable_node(nodes_data, closest_edge, coordinates)
    return closest_node


# Gets the direction of edges, returns (direction1, direction2), directions are bool
def get_direction_of_edges(
    edges_data,
    closest_edge_to_origin,
    closest_edge_to_destination,
):
    # Check if oneway or twoways
    starting_edge_direction = is_oneway(edges_data, closest_edge_to_origin)
    finishing_edge_direction = is_oneway(edges_data, closest_edge_to_destination)

    return (starting_edge_direction, finishing_edge_direction)


# Returns true if 2 edges are the same edge
def is_same_edge(oneway, edge1, edge2):
    # For oneway
    if oneway:
        if edge1 == edge2:
            return True
        return False
    else:
        if (edge1[0] == edge2[0] and edge1[1] == edge2[1]) or (
            edge1[0] == edge2[1] and edge1[1] == edge2[0]
        ):
            return True
        return False


# Returns true if oneway else false
def is_oneway(edges_data, edge):
    if edges_data.loc[(edge[0], edge[1]), "oneway"].item():
        # One way street
        return True
    else:
        # Two way
        return False


# Get the coordinates of a node returns (x,y)
def get_node_coordinates(nodes_data, node):
    # Extract info from the nodes df
    node_coordinates = nodes_data.loc[node, ["y", "x"]]
    x = node_coordinates.at["x"]
    y = node_coordinates.at["y"]

    return (x, y)


# Returns the closest node to the coordinates that is part of the found edge, returns node id
def assign_usable_node(nodes_data, found_edge, coordinates):
    # Get both coordinates
    node1_x, node1_y = get_node_coordinates(nodes_data, found_edge[0])
    node2_x, node2_y = get_node_coordinates(nodes_data, found_edge[1])

    marker_x = coordinates[1]
    marker_y = coordinates[0]

    node1_distance = dist([marker_x, marker_y], [node1_x, node1_y])
    node2_distance = dist([marker_x, marker_y], [node2_x, node2_y])

    return found_edge[0] if node1_distance < node2_distance else found_edge[1]


# Checks if a node is part of the found edge, returns bool
def is_node_in_edge(node, found_edge):
    # Node not part of the closest edge
    if node != found_edge[0] and node != found_edge[1]:
        return False
    return True


# Decides what will be the starting node for the route, checking if edge exists
# Also checks for the case where the closest node doesn't form part of the closest edge, in this case the edge takes priority
# Returns a list of tuples, (pre_start, starting_node) and the inverse if the road is two-ways else an empty tuple
def decide_starting_node_and_edge(
    nodes_data, edges_data, found_edge, closest_node, origin_coordinates
):
    closest_usable_node = closest_node

    # Node not part of the closest edge
    if closest_usable_node != found_edge[0] and closest_usable_node != found_edge[1]:
        print("case1 rare")
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
        print("oneway")
        # One way street
        return [(found_edge[0], found_edge[1]), ()]

    else:
        print("twoways")
        # Two way
        furthest_node = (
            found_edge[0] if found_edge[1] == closest_usable_node else found_edge[1]
        )

        return [
            (furthest_node, closest_usable_node),
            (closest_usable_node, furthest_node),
        ]


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
    print(
        "merging",
        pre,
        "and",
        coordinates,
        "and",
        post,
    )
    n = len(post)
    for i in range(n):
        if post[i] in pre and pre.index(post[i]) != len(pre) - 1:
            print("i", i)
            print()
            print("found", post[i])
            print("remaining", post[i:])
            return post[i:]

    return pre + coordinates + post


def get_segment_to_starting_node(
    graph, nodes_data, edges_data, origin_coordinates, origin_id
):
    found_edge = ox.distance.nearest_edges(
        graph, origin_coordinates[1], origin_coordinates[0]
    )

    print("found edge start", found_edge)
    print("closest edge start", origin_id)

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
        pre_route_info_option1[0]["coordinates"], 0.00001
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
            pre_route_info_option2[0]["coordinates"], 0.00001
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


def get_segment_to_finishing_node(
    graph, edges_data, destination_coordinates, destination_id
):
    found_edge = ox.distance.nearest_edges(
        graph, destination_coordinates[1], destination_coordinates[0]
    )
    print("found edge finish", found_edge)
    print("closest edge finish", destination_id)

    # Find the options for post and start, in case the node is in the route change start with post
    decided_nodes = decide_finishing_node_and_edge(
        edges_data, found_edge, destination_id
    )

    option1 = decided_nodes[0]
    option2 = decided_nodes[1]
    print(
        "nodes options",
        option1,
        option2,
    )

    # Get interpolation for option 1
    post_route_info_option1 = get_route_info_per_road(
        edges_data, [option1[0], option1[1]], coordinates=True
    )

    interpolated1 = ox.utils_geo.interpolate_points(
        post_route_info_option1[0]["coordinates"], 0.00001
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
            post_route_info_option2[0]["coordinates"], 0.00001
        )

        interpolated2 = list(interpolated2)

        finishing_index2 = get_closest_coordinate_index(
            interpolated2, destination_coordinates[1], destination_coordinates[0]
        )

        path_option2 = (
            find_path_from_destination_to_edge(interpolated2, finishing_index2),
            option2[0],
        )
    else:
        path_option2 = []
    print("finishing options1", path_option1)
    print("finishing options2", path_option2)
    print()
    return (path_option1, path_option2)


# Decides what will be the finishing node for the route, checking if edge exists
# Returns a list of tuples, (post_finish, finishing_node) and the inverse if the road is two-ways else an empty tuple
def decide_finishing_node_and_edge(edges_data, found_edge, closest_node):
    if edges_data.loc[(found_edge[0], found_edge[1]), "oneway"].item():
        print("oneway")
        # One way street
        return [(found_edge[0], found_edge[1]), ()]

    else:
        print("twoways")
        # Two way
        furthest_node = (
            found_edge[0] if found_edge[1] == closest_node else found_edge[1]
        )
        print("stuff", (furthest_node, closest_node), (closest_node, furthest_node))
        return [(furthest_node, closest_node), (closest_node, furthest_node)]


# Returns a lat long location of a coordinate snapped to an edge
def snap_to_closest_road(linestring, lat, long):
    nearest_point = linestring.interpolate(linestring.project(Point(long, lat)))
    distance = geopy.distance.distance((lat, long), nearest_point.coords[0]).meters
    if distance < min_distance:
        snapped_location = nearest_point.coords[0]
        min_distance = distance
    return snapped_location


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
    edge_geometry = edges_data.loc[(node1, node2), "geometry"]
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

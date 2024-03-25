from os import close
import matplotlib.pyplot as plt
import geopandas as gpd
import networkx as nx
import numpy as np
import osmnx as ox
from math import dist
from shapely.geometry import LineString
import osmnx.utils_geo as og


def plot_and_select_nodes(graph):
    # Plot the graph
    fig, ax = ox.plot_graph(
        graph, node_color="blue", node_size=10, show=False, close=False
    )

    # Allow the user to interactively click on two nodes
    selected_nodes = plt.ginput(2, timeout=0)

    # Convert clicked coordinates to nearest nodes
    selected_node_ids = [
        ox.distance.nearest_nodes(graph, x, y) for x, y in selected_nodes
    ]

    # Close the plot
    plt.close()

    return selected_node_ids


def create_graph():
    graph = ox.graph_from_point((37.9814, -84.49699), dist=200, network_type="drive")
    ox.save_graphml(graph, "./point_graph.graphml")


def get_all_data(graph):
    for node, data in graph.nodes(data=True):
        print(node, data)

    # Access edge data
    print("\nEdge Data:")
    for u, v, key, data in graph.edges(keys=True, data=True):
        print(f"Edge ({u}, {v}, {key}), Data: {data}")


def get_coordinates(graph, node_id):
    # Retrieve node attributes, including latitude and longitude
    node_data = graph.nodes[node_id]
    latitude = node_data["y"]
    longitude = node_data["x"]
    return latitude, longitude


def plot_route(graph, route):
    # Get coordinates for each node in the route
    coordinates = [get_coordinates(graph, node_id) for node_id in route]

    # Plot the graph
    ox.plot_graph(graph, show=False, close=False)

    # Plot lines connecting the nodes along the route
    for i in range(len(coordinates) - 1):
        origin_coords = coordinates[i]
        end_coords = coordinates[i + 1]
        plt.plot(
            [start_coords[1], end_coords[1]],
            [start_coords[0], end_coords[0]],
            color="red",
            linewidth=2,
        )

    # Plot start and end points
    start_coords = coordinates[0]
    end_coords = coordinates[-1]
    plt.scatter(
        [start_coords[1], end_coords[1]],
        [start_coords[0], end_coords[0]],
        color="red",
        s=50,
        zorder=5,
    )

    # Show the plot
    plt.show()


def load_graph_nx(filepath):
    graph = nx.read_graphml(filepath)
    return graph


def plot_edge_route(graph, coords):
    # Plot the graph
    ox.plot_graph(graph, show=False, close=False)

    # Plot lines connecting the nodes along the route
    for i in range(len(coords) - 1):
        start_coords = coords[i]
        print(start_coords)
        end_coords = coords[i + 1]
        print(end_coords)
        plt.plot(
            [start_coords[1], end_coords[1]],
            [start_coords[0], end_coords[0]],
            color="red",
            linewidth=2,
        )

    # Plot start and end points
    start_coords = coords[0]
    end_coords = coords[-1]
    plt.scatter(
        [start_coords[1], end_coords[1]],
        [start_coords[0], end_coords[0]],
        color="green",
        s=50,
        zorder=5,
    )

    # Show the plot
    plt.show()


def testing():
    graph = load_graph()

    # Plot and select nodes interactively
    selected_nodes = plot_and_select_nodes(graph)

    # Perform any additional operations with the selected nodes if needed
    route = shortest(graph, selected_nodes)

    plot_route(graph, route)


def test():
    # Load the graph data
    graph = load_graph("./point_graph.graphml")

    # Plot and select nodes for the origin and destination
    origin_destination = plot_and_select_nodes(graph)

    # Find the shortest route between the origin and destination nodes
    route = shortest(graph, origin_destination)

    # Get edge data from the graph to extract LineString geometry
    edge_data = ox.graph_to_gdfs(graph, nodes=False, edges=True)

    line_string = edge_data["geometry"].iloc[1]

    line_string_coords = line_string.coords

    plot_edge_route(graph, line_string_coords)


def draw_line(graph, coords):
    pos = {node: (lon, lat) for node, (lon, lat) in enumerate(coords)}

    nx.draw(graph, pos, with_labels=True, font_weight="bold", node_size=10)
    nx.draw_networkx_edges(
        graph,
        pos,
        edge_list=[(i, i + 1) for i in range(len(coords) - 1)],
        edge_color="r",
        width=2,
    )

    plt.show()


def plot_line(coordinates):
    # Unpack the coordinates into separate lists
    x_values, y_values = zip(*coordinates)

    # Plot the line
    plt.plot(x_values, y_values, label="My Line")

    # Add labels and title
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Line Plot Example")

    # Show the legend
    plt.legend()

    # Display the plot
    plt.show()


def test_nx():
    coordinates = [
        (-84.498433, 37.980544),
        (-84.4983078, 37.9806978),
        (-84.498289, 37.980721),
        (-84.498238, 37.980771),
        (-84.498147, 37.98084),
        (-84.498074, 37.98088),
        (-84.497948, 37.980937),
        (-84.4978953, 37.980953),
        (-84.497662, 37.981024),
        (-84.497541, 37.981074),
        (-84.497447, 37.981128),
        (-84.497347, 37.981208),
        (-84.497307, 37.98125),
        (-84.497248, 37.981339),
        (-84.49722, 37.981396),
        (-84.497195, 37.981467),
        (-84.4971686, 37.9815627),
        (-84.4971311, 37.9816986),
        (-84.497126, 37.981717),
        (-84.497101, 37.981772),
        (-84.497073, 37.981819),
        (-84.497008, 37.981903),
        (-84.4969953, 37.9819155),
        (-84.496917, 37.981992),
        (-84.4968529, 37.9820419),
    ]

    plot_line(coordinates)


def load_multidigraph(filepath):
    # Load a graph (replace with your graph file or creation method)
    graph = ox.load_graphml(filepath=filepath)
    graph = ox.add_edge_speeds(graph)
    return ox.speed.add_edge_travel_times(graph)


# Returns list of node IDs
def select_origin_destination_nodes(graph):
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


def select_origin_coordinates(graph):
    # Plot the graph
    ox.plot_graph(graph, node_color="blue", node_size=10, show=False, close=False)

    # Allow the user to interactively click on one place
    selected_coordinate = plt.ginput(1, timeout=0)

    if not selected_coordinate:
        return None

    x, y = selected_coordinate[0]

    # Close the plot
    plt.close()

    return x, y


# Returns route's nodes information as a list
def get_shortest_route(graph, origin_node_id, destination_node_id):
    return ox.shortest_path(graph, origin_node_id, destination_node_id)


# Returns a dictionary
def get_route_info_per_road(
    graph, route, coordinates=False, highway=False, maxspeed=False, length=False
):
    if not coordinates and not highway and not maxspeed and not length:
        return []

    edges_data = ox.graph_to_gdfs(graph, nodes=False, edges=True)
    edges_data = edges_data.sort_index(level=["u", "v"])

    print(edges_data.loc[(65307376, 65319940)])

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
    return list(linestring.coords)


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


def extract_data_for_api(graph):
    for node in graph.nodes:
        for neighbor, edge_data in graph[node].items():
            print(node)
    for edge in graph.edges:
        print(edge)

    return 0


def extract():
    graph = load_multidigraph("./test-graph.graphml")
    nodes, edges = extract_data_for_api(graph)
    print(nodes)
    print()
    print(edges)


def main():
    graph = load_multidigraph("./test-graph.graphml")
    origin, destination = select_origin_destination_nodes(graph)
    if origin is None or destination is None:
        print("here")
        return
    print(dijkstra_algorithm(graph, origin, destination))
    route = get_shortest_route(graph, origin, destination)
    route_info = get_route_info_per_road(graph, route, coordinates=True)


def get_segment_to_nearest_node(graph, origin_coordinates, origin_id):
    origin_edge = ox.distance.nearest_edges(
        graph, origin_coordinates[1], origin_coordinates[0]
    )
    pre_origin = origin_edge[0] if origin_edge[1] == origin_id else origin_edge[1]

    pre_route_info = get_route_info_per_road(
        graph, [pre_origin, origin_id], coordinates=True
    )
    pre_coordinates = [
        coordinate for street in pre_route_info for coordinate in street["coordinates"]
    ]

    starting_index = get_closest_coordinate_index(
        pre_coordinates, origin_coordinates[1], origin_coordinates[0]
    )

    return find_path_from_edge_to_origin(pre_coordinates, starting_index)


def get_closest_coordinate_index(coordinates, x, y):
    closest = {"index": 0, "distance": float("inf")}

    for i in range(len(coordinates)):
        xy_points = [point for point in coordinates[i]]
        curr_dist = dist(xy_points, [x, y])
        if curr_dist < closest["distance"]:
            closest["index"] = i
            closest["distance"] = curr_dist
    return closest["index"]


def find_path_from_edge_to_origin(linestring, starting_index):
    coords = []
    for i in range(starting_index, len(linestring)):
        coords.append(linestring[i])
    return coords


def precise():
    graph = load_multidigraph("./point_graph.graphml")
    origin, destination = select_origin_destination_nodes(graph)
    x, y = select_origin_coordinates(graph)
    print(x, y)

    nearest_edge = ox.distance.nearest_edges(graph, x, y)
    print(nearest_edge)

    a, b, c = nearest_edge
    furthest = a if b == origin else b

    route_info = get_route_info_per_road(graph, [furthest, origin], coordinates=True)

    coordinates = [
        coordinate for street in route_info for coordinate in street["coordinates"]
    ]
    closest = {"index": 0, "distance": float("inf")}

    for i in range(len(coordinates)):
        coords = [x for x in coordinates[i]]
        curr_dist = dist(coords, [x, y])
        if curr_dist < closest["distance"]:
            closest["index"] = i
            closest["distance"] = curr_dist

    print(closest)

    path = find_path_from_edge_to_origin(coordinates, closest["index"])

    draw_line(graph, path)


def merge_lists(coordinates, pre):
    n = len(pre)
    missing = []
    index = 0
    for i in range(n):
        if pre[i] not in coordinates:
            missing.append(pre[i])
        else:
            index = coordinates.index(pre[i])
            break

    merged = missing + coordinates[index:]

    return merged


def optimize_route(pre_route, route, post_route):
    full_route = pre_route + route + post_route
    visited_nodes = set()
    loop_detected = False
    optimized_route = []

    for node in full_route:
        if node in visited_nodes:
            loop_detected = True
            break
        else:
            visited_nodes.add(node)

    if loop_detected:
        optimized_route = find_optimal_route(pre_route, route, post_route)
    else:
        optimized_route = pre_route + route + post_route

    return optimized_route


def find_optimal_route(pre_route, route, post_route):
    loop_start = find_start_of_loop(route)
    optimized_route = []

    for node in pre_route:
        if node == loop_start:
            break
        else:
            optimized_route.append(node)

    for node in post_route:
        if node == loop_start:
            break
        else:
            optimized_route.append(node)

    return optimized_route


def find_start_of_loop(route):
    visited_nodes = set()

    for node in route:
        if node in visited_nodes:
            return node
        else:
            visited_nodes.add(node)

    return None


if __name__ == "__main__":
    main()

from flask import Flask, jsonify
from flask_cors import CORS
import osmnx as ox
import matplotlib.pyplot as plt
import networkx as nx
import json

app = Flask(__name__)
CORS(app)


@app.route("/first-test")
def first_test():
    # Read the .graphml file content
    graphml_content = read_graphml_file_content()

    # Pass the content as JSON
    return graphml_content


def read_graphml_file_content():
    # Open the .graphml file and read its content
    file_path = 'C:/Users/Milo/OneDrive/Escritorio/ROAD/Portfolio/tms/tms-server/data.json'
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


# Returns a dictionary
def get_route_info_per_road(graph, route):
    edges_data = ox.graph_to_gdfs(graph, nodes=False, edges=True)
    edges_data = edges_data.sort_index(level=["u", "v"])

    route_info = []

    for i in range(len(route) - 1):
        road_info = {
            "coordinates": get_edge_coordinates(edges_data, route[i], route[i + 1]),
            "highway": get_edge_highway(edges_data, route[i], route[i + 1]),
            "maxspeed": get_edge_maxspeed(edges_data, route[i], route[i + 1]),
            "length": get_edge_length(edges_data, route[i], route[i + 1]),
        }
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
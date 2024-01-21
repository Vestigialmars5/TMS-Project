import matplotlib.pyplot as plt
import geopandas as gpd
import networkx as nx
import osmnx as ox


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
    for i in range(len(coordinates)-1):
        start_coords = coordinates[i]
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


def main():
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
    return ox.load_graphml(filepath=filepath)


# Returns list of node IDs
def select_origin_destination(graph):
    # Plot the graph
    tmp = ox.plot_graph(
        graph, node_color="blue", node_size=10, show=False, close=False
    )  # returns fig, ax tuple hence the tmp

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


# Returns a list of tuples
def get_coordinates_for_route(graph, route):
    edges_data = ox.graph_to_gdfs(graph, nodes=False, edges=True)
    edges_data = edges_data.sort_index(level=["u", "v"])

    all_coordinates = []

    for i in range(len(route) - 1):
        all_coordinates += get_edge_coordinates(edges_data, route[i], route[i + 1])

    return all_coordinates


# To get the exact coordinates that make an edge
def get_edge_coordinates(edges_data, node1, node2):
    edge_geometry = edges_data.loc[(node1, node2), "geometry"]
    linestring = edge_geometry.iloc[0]
    return list(linestring.coords)


def testing():
    graph = load_multidigraph("./point_graph.graphml")
    origin, destination = select_origin_destination(graph)
    if origin == None or origin == None:
        print("here")
        return
    route = get_shortest_route(graph, origin, destination)
    coords = get_coordinates_for_route(graph, route)
    plot_line(coords)


if __name__ == "__main__":
    testing()

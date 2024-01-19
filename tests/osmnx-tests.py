import matplotlib.pyplot as plt
import geopandas as gpd
import networkx as nx
import osmnx as ox


def plot_and_select_nodes(graph):
    # Plot the graph
    fig, ax = ox.plot_graph(graph, node_color='blue',
                            node_size=10, show=False, close=False)

    # Allow the user to interactively click on two nodes
    selected_nodes = plt.ginput(2, timeout=0)

    # Convert clicked coordinates to nearest nodes
    selected_node_ids = [ox.distance.nearest_nodes(
        graph, x, y) for x, y in selected_nodes]

    # Close the plot
    plt.close()

    return selected_node_ids


def shortest(graph, nodes):
    route = ox.shortest_path(graph, nodes[0], nodes[1])
    ox.plot_graph_route(graph, route, node_color="red")
    return route

def create_graph():
    graph = ox.graph_from_point((37.9814, -84.49699), dist=200, network_type="drive")
    ox.save_graphml(graph, "./point_graph.graphml")

def load_graph(filepath):
    # Load a graph (replace with your graph file or creation method)
    return ox.load_graphml(filepath=filepath)


def get_all_data(graph):
    for node, data in graph.nodes(data=True):
        print(node, data)

    # Access edge data
    print("\nEdge Data:")
    for u, v, key, data in graph.edges(keys=True, data=True):
        print(f"Edge ({u}, {v}, {key}), Data: {data}")


def print_data():
    graph = load_graph()
    get_all_data(graph)


def get_coordinates(graph, node_id):
    # Retrieve node attributes, including latitude and longitude
    node_data = graph.nodes[node_id]
    latitude = node_data['y']
    longitude = node_data['x']
    return latitude, longitude


def plot_route(graph, route):

    # Get coordinates for each node in the route
    coordinates = [get_coordinates(graph, node_id) for node_id in route]

    # Plot the graph
    ox.plot_graph(graph, show=False, close=False)

    # Plot lines connecting the nodes along the route
    for i in range(1):
        start_coords = coordinates[i]
        end_coords = coordinates[i + 1]
        plt.plot([start_coords[1], end_coords[1]], [
                 start_coords[0], end_coords[0]], color='red', linewidth=2)

    # Plot start and end points
    start_coords = coordinates[0]
    end_coords = coordinates[-1]
    plt.scatter([start_coords[1], end_coords[1]], [
                start_coords[0], end_coords[0]], color='green', s=50, zorder=5)

    # Show the plot
    plt.show()


def plot_edge_route(graph, coords):
    # Plot the graph
    ox.plot_graph(graph, show=False, close=False)

    # Plot lines connecting the nodes along the route
    for i in range(len(coords)-1):
        start_coords = coords[i]
        print(start_coords)
        end_coords = coords[i + 1]
        print(end_coords)
        plt.plot([start_coords[1], end_coords[1]], [
            start_coords[0], end_coords[0]], color='red', linewidth=2)

    # Plot start and end points
    start_coords = coords[0]
    end_coords = coords[-1]
    plt.scatter([start_coords[1], end_coords[1]], [
                start_coords[0], end_coords[0]], color='green', s=50, zorder=5)

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

def load_graph_nx(filepath):
    graph = nx.read_graphml(filepath)
    return graph

def draw_line(graph, coords):
    pos = {node: (lon, lat) for node, (lon, lat) in enumerate(coords)}

    nx.draw(graph, pos, with_labels=True, font_weight="bold", node_size=10)
    nx.draw_networkx_edges(graph, pos, edge_list=[(i, i+1) for i in range(len(coords) -1)], edge_color="r", width=2)

    plt.show()


def plot_line(coordinates):
    # Unpack the coordinates into separate lists
    x_values, y_values = zip(*coordinates)

    # Plot the line
    plt.plot(x_values, y_values, label='My Line')

    # Add labels and title
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Line Plot Example')

    # Show the legend
    plt.legend()

    # Display the plot
    plt.show()


def test_nx():
    coordinates = [(-84.498433, 37.980544), (-84.4983078, 37.9806978), (-84.498289, 37.980721), (-84.498238, 37.980771), (-84.498147, 37.98084), (-84.498074, 37.98088), (-84.497948, 37.980937), (-84.4978953, 37.980953), (-84.497662, 37.981024), (-84.497541, 37.981074), (-84.497447, 37.981128), (-84.497347, 37.981208), (-84.497307, 37.98125), (-84.497248, 37.981339), (-84.49722, 37.981396), (-84.497195, 37.981467), (-84.4971686, 37.9815627), (-84.4971311, 37.9816986), (-84.497126, 37.981717), (-84.497101, 37.981772), (-84.497073, 37.981819), (-84.497008, 37.981903), (-84.4969953, 37.9819155), (-84.496917, 37.981992), (-84.4968529, 37.9820419)]

    plot_line(coordinates)

if __name__ == "__main__":
    test()

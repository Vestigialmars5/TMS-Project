import mplleaflet
import matplotlib.pyplot as plt
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


def main():
    # Load a graph (replace with your graph file or creation method)
    graph = ox.load_graphml(filepath="./test-graph.graphml")

    # Plot and select nodes interactively
    selected_nodes = plot_and_select_nodes(graph)

    # Perform any additional operations with the selected nodes if needed
    shortest(graph, selected_nodes)

if __name__ == "__main__":
    main()

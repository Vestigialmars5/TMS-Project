import osmnx as ox
from math import dist
from shapely.geometry import LineString

GRAPH = "./test-graph.graphml"


def main():
    # Retrieved as lat, long (normally gotten from a post request)
    # Oneway street case
    origin_coordinates = [37.79109950401872, -122.4096465110779]
    destination_coordinates = [37.79067577012899, -122.41325139999391]

    # Loads graph
    graph = ox.load_graphml(filepath=GRAPH)
    graph = ox.add_edge_speeds(graph)
    graph = ox.speed.add_edge_travel_times(graph)

    # Closest node to the coordinate input (x,y)
    origin_id = ox.distance.nearest_nodes(
        graph, origin_coordinates[1], origin_coordinates[0]
    )
    destination_id = ox.distance.nearest_nodes(
        graph, destination_coordinates[1], destination_coordinates[0]
    )

    # List of coordinates that make up the route from a starting point to a finishing point (for a polyline in leaflet)
    coordinates = calculate_route_coordinates(
        graph,
        origin_id,
        destination_id,
        origin_coordinates,
        destination_coordinates,
    )

    return coordinates


# Calculates the coordinates along the route including pre and post (excluded logic for destination segment for simplicity)
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

    # Get coordinates and a new origin node to get precise starting location
    # Each option has the coordinates from a point to a target node, and the target node
    direction1, direction2 = get_segment_to_starting_node(
        graph, nodes_data, edges_data, origin_coordinates, origin_id
    )

    new_origin_id = direction1[1]

    # Calculate the route from the new origin to the new destination
    route = ox.shortest_path(graph, new_origin_id, destination_id)

    # Segments in between the edges
    pre_coordinates = direction1[0]

    if direction2:
        # Check if second node is the second starting option, this takes care of going to the target node and coming back throught
        # that same direction. Changing to second option just switches the direction (doesn't handle twoway roads, same edge cases)
        if len(route) > 1 and route[1] == direction2[1]:
            # Makes starting node option2 start
            route.pop(0)
            pre_coordinates = direction2[0]

    route_info = get_route_info_per_road(edges_data, route)

    # Extract coordinates into usable list
    coordinates = []
    for road in route_info:
        coordinates += list(road["coordinates"].coords)

    # Return the list of coordinates that makes up the full route
    return pre_coordinates + coordinates


# Gets the segment between the closest point in the coordinate on the edge, to the node
def get_segment_to_starting_node(
    graph, nodes_data, edges_data, origin_coordinates, origin_id
):
    found_edge = ox.distance.nearest_edges(
        graph, origin_coordinates[1], origin_coordinates[0]
    )

    # Find the options for node before starting node (pre) and starting node (start), in case the node is in the route change start with pre
    decided_nodes = decide_starting_node_and_edge(
        nodes_data, edges_data, found_edge, origin_id, origin_coordinates
    )
    # a->b and b->a, second option empty if oneway
    option1 = decided_nodes[0]
    option2 = decided_nodes[1]

    print(option1, option2)

    # Get interpolation for option 1
    pre_route_info_option1 = get_route_info_per_road(
        edges_data, [option1[0], option1[1]]
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
            edges_data, [option2[0], option2[1]]
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


# Decides what will be the starting node for the route, checking if edge exists
# Also checks for the case where the closest node doesn't form part of the closest edge, in this case the edge takes priority
# Returns a list of tuples, (pre_start, starting_node) and the inverse if the road is two-ways else an empty tuple
def decide_starting_node_and_edge(
    nodes_data, edges_data, found_edge, closest_node, origin_coordinates
):
    closest_usable_node = closest_node

    # Node not part of the closest edge, getting new node based on distance from coordinate
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


# Returns a list of dictionaries with specific information for each road (this function handles some other information retrieval, excluded)
def get_route_info_per_road(edges_data, route):

    route_info = []
    for i in range(len(route) - 1):
        road_info = {}

        road_info["coordinates"] = get_edge_coordinates(
            edges_data, route[i], route[i + 1]
        )
        route_info.append(road_info)

    return route_info


# To get the exact coordinates that make an edge
def get_edge_coordinates(edges_data, node1, node2):
    edge_geometry = edges_data.loc[(node1, node2), "geometry"]
    linestring = edge_geometry.iloc[0]
    linestring_list = list(linestring.coords)
    sorted_lat_long = [(lat, long) for long, lat in linestring_list]
    return LineString(sorted_lat_long)


# Returns the index of the point closest to the coordinate
def get_closest_coordinate_index(coordinates, x, y):
    closest = {"index": 0, "distance": float("inf")}

    for i in range(len(coordinates)):
        xy_points = [point for point in coordinates[i]]
        curr_dist = dist(xy_points, [y, x])
        if curr_dist < closest["distance"]:
            closest["index"] = i
            closest["distance"] = curr_dist

    return closest["index"]


# Returns a list of coordinates that make up the segment from the point in between the edge and the target node
def find_path_from_edge_to_origin(linestring, starting_index):
    coords = []
    for i in range(starting_index, len(linestring)):
        coords.append(linestring[i])
    return coords


if __name__ == "__main__":
    main()

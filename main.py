import graph as gr
import sys

# Create a new graph
# graph = gr.Graph()

file_path = sys.argv[1]  # Path to the input graph file
graph = gr.read_graph_file(file_path)

# Apply Dijkstra's algorithm
# start_vertex = '1'
# distances = graph.dijkstra(start_vertex)

# # Print the shortest distances from the start_vertex
# for vertex, distance in distances.items():
#     print(f"Shortest distance from {start_vertex} to {vertex}: {distance}")
# print(graph)




# minimum_spanning_tree = graph.kruskal()
# print(minimum_spanning_tree)

# Print the minimum spanning tree
# for vertex, connections in minimum_spanning_tree.vertices.items():
#     for neighbor, weight in connections.items():
#         print(f"Edge: {vertex} - {neighbor}, Weight: {weight}")

# Apply the Ford-Fulkerson algorithm
max_flow, flow_values = graph.ford_fulkerson_algorithm()

# Print the maximum flow
print("Maximum Flow:", max_flow)

# Print the flow values for each edge
for vertex, connections in flow_values.items():
    for neighbor, flow in connections.items():
        print(f"Edge: {vertex} - {neighbor}, Flow: {flow}")
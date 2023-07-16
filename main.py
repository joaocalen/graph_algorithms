import graph as gr
import sys

# Create a new graph
# graph = gr.Graph()

file_path = sys.argv[1]  # Path to the input graph file
graph = gr.read_graph_file(file_path)

# Add vertices
# graph.add_vertex("A")
# graph.add_vertex("B")
# graph.add_vertex("C")
# graph.add_vertex("D")
# graph.add_vertex("E")
# graph.add_vertex("F")
# graph.add_vertex("G")

# # Add weighted edges
# graph.add_edge("A", "B", 7)
# graph.add_edge("A", "D", 5)
# graph.add_edge("B", "C", 8)
# graph.add_edge("B", "D", 9)
# graph.add_edge("B", "E", 7)
# graph.add_edge("C", "E", 5)
# graph.add_edge("D", "E", 15)
# graph.add_edge("D", "F", 6)
# graph.add_edge("E", "F", 8)
# graph.add_edge("E", "G", 9)
# graph.add_edge("F", "G", 11)


# Apply Dijkstra's algorithm
start_vertex = '1'
distances = graph.dijkstra(start_vertex)

# # Print the shortest distances from the start_vertex
for vertex, distance in distances.items():
    print(f"Shortest distance from {start_vertex} to {vertex}: {distance}")
print(graph)




# minimum_spanning_tree = graph.kruskal()
# print(minimum_spanning_tree)

# Print the minimum spanning tree
# for vertex, connections in minimum_spanning_tree.vertices.items():
#     for neighbor, weight in connections.items():
#         print(f"Edge: {vertex} - {neighbor}, Weight: {weight}")
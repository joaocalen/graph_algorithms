import graph as gr

# Create a new graph
graph = gr.Graph()

# Add vertices
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")

# Add weighted edges
graph.add_edge("A", "B", 4)
graph.add_edge("A", "C", 2)
graph.add_edge("B", "C", 1)
graph.add_edge("B", "D", 5)
graph.add_edge("C", "D", 8)
graph.add_edge("C", "E", 10)
graph.add_edge("D", "E", 2)

# Apply Dijkstra's algorithm
start_vertex = "A"
distances = graph.dijkstra(start_vertex)

# Print the shortest distances from the start_vertex
for vertex, distance in distances.items():
    print(f"Shortest distance from {start_vertex} to {vertex}: {distance}")
print(graph)
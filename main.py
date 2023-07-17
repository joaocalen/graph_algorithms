import graph as gr
import sys

# Create a new graph
# graph = gr.Graph()

file_path = sys.argv[1]  # Path to the input graph file
graph = gr.read_graph_file(file_path)

algorithm = int(sys.argv[2])

if algorithm == 1:
    print("Calculating Dijkstra...")
    start_vertex = sys.argv[3]
    distances = graph.dijkstra(start_vertex)

    print("Given the Graph G:")
    print(graph)
    # Print the shortest distances from the start_vertex
    for vertex, distance in distances.items():
        print(f"Shortest distance from {start_vertex} to {vertex}: {distance}")
    
elif algorithm == 2:
    print("Calculating Kruskal...")
    mst_cost, minimum_spanning_tree = graph.kruskal()
    print("Printing MST:")
    print(minimum_spanning_tree)    

    # Print the minimum spanning tree
    for vertex, connections in minimum_spanning_tree.vertices.items():
        for neighbor, weight in connections.items():
            print(f"Edge: {vertex} - {neighbor}, Weight: {weight}")
    print("MST Cost: ")
    print(mst_cost)
else:
    print("Calculating Maximum flow...")
    # Apply the Ford-Fulkerson algorithm
    max_flow, flow_values = graph.ford_fulkerson_algorithm()

    # Print the maximum flow
    print("Maximum Flow:", max_flow)

    # Print the flow values for each edge
    for vertex, connections in flow_values.items():
        for neighbor, flow in connections.items():
            print(f"Edge: {vertex} - {neighbor}, Flow: {flow}")





import heapq
from collections import deque

class Graph:
    def __init__(self, directed=False):
        self.vertices = {}  # Dictionary to store the vertices and their connections
        self.directed = directed # True if it's a directed graph. False otherwise.
    
    def add_vertex(self, vertex):
        self.vertices[vertex] = {}  # Initialize an empty dictionary to store the connections and their weights
    
    def add_edge(self, start_vertex, end_vertex, weight):
        if start_vertex in self.vertices and end_vertex in self.vertices:
            self.vertices[start_vertex][end_vertex] = weight  # Add the weighted edge from start_vertex to end_vertex
            if not self.directed:
                self.vertices[end_vertex][start_vertex] = weight  # Add the weighted edge from end_vertex to start_vertex
            else:
                self.vertices[end_vertex][start_vertex] = 0  # Add the weighted edge from end_vertex to start_vertex
    def __str__(self):
        graph_str = ""
        for vertex in self.vertices:
            neighbors = self.vertices[vertex]
            neighbors_str = ", ".join([f"{neighbor} ({weight})" for neighbor, weight in neighbors.items()])
            graph_str += f"{vertex}: {neighbors_str}\n"
        return graph_str

    def dijkstra(self, start_vertex):
        distances = {vertex: float('inf') for vertex in self.vertices}  # Initialize distances to all vertices as infinity
        distances[start_vertex] = 0  # Set the distance to the start_vertex as 0
        heap = [(0, start_vertex)]  # Create a priority queue (heap) with initial distance and start_vertex
        heapq.heapify(heap)
        visited = set()
        
        while heap:
            current_distance, current_vertex = heapq.heappop(heap)  # Get the vertex with the smallest distance
            visited.add(current_vertex)
            
            for neighbor, weight in self.vertices[current_vertex].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))
        
        return distances

    def find(self, parent, vertex):
        if parent[vertex] == vertex:
            return vertex
        return self.find(parent, parent[vertex])
    
    def union(self, parent, rank, vertex1, vertex2):
        root1 = self.find(parent, vertex1)
        root2 = self.find(parent, vertex2)
        
        if rank[root1] < rank[root2]:
            parent[root1] = root2            
        elif rank[root1] > rank[root2]:
            parent[root2] = root1            
        else:
            parent[root2] = root1
            rank[root1] += 1

    def kruskal(self):
        parent = {}  # Dictionary to store the parent of each vertex for finding cycles
        rank = {}  # Dictionary to store the rank of each vertex for union by rank
        mst_cost = 0
        
        for vertex in self.vertices:
            parent[vertex] = vertex
            rank[vertex] = 0
        
        edges = []
        for start_vertex, connections in self.vertices.items():
            for end_vertex, weight in connections.items():
                edges.append((start_vertex, end_vertex, weight))
        
        edges.sort(key=lambda x: x[2])  # Sort the edges in ascending order based on weight        
        minimum_spanning_tree = Graph()  # Graph to store the minimum spanning tree
        
        for edge in edges:
            start_vertex, end_vertex, weight = edge            
            root1 = self.find(parent, start_vertex)
            root2 = self.find(parent, end_vertex)
            
            if root1 != root2:  # If adding the edge does not form a cycle
                if start_vertex not in minimum_spanning_tree.vertices:
                    minimum_spanning_tree.add_vertex(start_vertex)                
                if end_vertex not in minimum_spanning_tree.vertices:
                    minimum_spanning_tree.add_vertex(end_vertex)
                minimum_spanning_tree.add_edge(start_vertex, end_vertex, weight)
                mst_cost += weight                
                
                self.union(parent, rank, root1, root2)
        
        return mst_cost, minimum_spanning_tree
    
class MaxFlowGraph(Graph):
    def __init__(self):
        super().__init__(directed=True)
        self.s = None  # Source vertex
        self.t = None  # Sink vertex

    def set_source(self, source):
        self.s = source

    def set_sink(self, sink):
        self.t = sink
    
    def bfs(self, parent):
        visited = set()
        queue = deque()

        # Start from the source vertex
        visited.add(self.s)
        queue.append(self.s)

        while queue:
            current_vertex = queue.popleft()
            for neighbor, capacity in self.residual_graph.vertices[current_vertex].items():                
                if neighbor not in visited and capacity > 0:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    parent[neighbor] = current_vertex

                    # Stop BFS if the sink vertex is reached
                    if neighbor == self.t:
                        return True

        return False

    def ford_fulkerson_algorithm(self):
        self.residual_graph = MaxFlowGraph()
        for vertex in self.vertices:
            self.residual_graph.add_vertex(vertex)
        for vertex in self.vertices:
            for neighbor, capacity in self.vertices[vertex].items():
                if capacity > 0:
                    self.residual_graph.add_edge(vertex, neighbor, capacity)
        
        max_flow = 0
        parent = {}

        while self.bfs(parent):
            # Find the minimum capacity along the augmenting path
            path_flow = float('inf')
            current_vertex = self.t

            while current_vertex != self.s:
                previous_vertex = parent[current_vertex]
                path_flow = min(path_flow, self.residual_graph.vertices[previous_vertex][current_vertex])
                current_vertex = previous_vertex

            # Update the residual capacities and reverse edges along the augmenting path
            current_vertex = self.t

            while current_vertex != self.s:
                previous_vertex = parent[current_vertex]
                self.residual_graph.vertices[previous_vertex][current_vertex] -= path_flow
                self.residual_graph.vertices[current_vertex][previous_vertex] += path_flow
                current_vertex = previous_vertex

            max_flow += path_flow

        print("Maximum Flow Graph:")
        print(self)
        print("Residual Graph:")
        print(self.residual_graph)
        flow_values = {}
        for vertex, connections in self.vertices.items():
            flow_values[vertex] = {}

            for neighbor, _ in connections.items():
                if self.vertices[vertex][neighbor] > 0:
                    flow_values[vertex][neighbor] = (
                        self.vertices[vertex][neighbor] - self.residual_graph.vertices[vertex][neighbor]
                    )

        return max_flow, flow_values

# Outside the class

def read_graph_file(file_path):
    graph = None
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('c'):
                continue  # Skip comment lines
            elif line.startswith('p'):
                _, type, num_vertices, num_edges = line.split()                
                num_vertices = int(num_vertices)
                num_edges = int(num_edges)
                if type == "max":
                    graph = MaxFlowGraph() # Define the graph to a directed graph
                else:
                    graph = Graph()
                for vertex in range(1, num_vertices + 1):                    
                    graph.add_vertex(str(vertex))
            elif line.startswith('a'):
                _, start_vertex, end_vertex, weight = line.split()
                graph.add_edge(start_vertex, end_vertex, int(weight))
            elif line.startswith('n'):
                _, vertex_id, vertex_type = line.split()
                vertex_id = str(vertex_id)
                if vertex_type == 's':
                    graph.set_source(vertex_id)
                elif vertex_type == 't':
                    graph.set_sink(vertex_id)
                
    return graph

import heapq

class Graph:
    def __init__(self):
        self.vertices = {}  # Dictionary to store the vertices and their connections
    
    def add_vertex(self, vertex):
        self.vertices[vertex] = {}  # Initialize an empty dictionary to store the connections and their weights
    
    def add_edge(self, start_vertex, end_vertex, weight):
        if start_vertex in self.vertices and end_vertex in self.vertices:
            self.vertices[start_vertex][end_vertex] = weight  # Add the weighted edge from start_vertex to end_vertex
            self.vertices[end_vertex][start_vertex] = weight  # Add the weighted edge from end_vertex to start_vertex
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
            # print("For edge: " + str(edge))
            start_vertex, end_vertex, weight = edge
            
            root1 = self.find(parent, start_vertex)
            root2 = self.find(parent, end_vertex)
            # print("root 1: " + str(root1) + " rank: " + str(rank[root1]) + ", root 2: " + str(root2) + " rank: " + str(rank[root2]))

            
            if root1 != root2:  # If adding the edge does not form a cycle
                if start_vertex not in minimum_spanning_tree.vertices:
                    minimum_spanning_tree.add_vertex(start_vertex)                
                if end_vertex not in minimum_spanning_tree.vertices:
                    minimum_spanning_tree.add_vertex(end_vertex)
                minimum_spanning_tree.add_edge(start_vertex, end_vertex, weight)                
                
                self.union(parent, rank, root1, root2)
        
        return minimum_spanning_tree
    

# Outside the class

def read_graph_file(file_path):
    graph = Graph()
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('c'):
                continue  # Skip comment lines
            elif line.startswith('p'):
                _, _, num_vertices, num_edges = line.split()
                num_vertices = int(num_vertices)
                num_edges = int(num_edges)
                for vertex in range(1, num_vertices + 1):
                    graph.add_vertex(str(vertex))
            elif line.startswith('a'):
                _, start_vertex, end_vertex, weight = line.split()
                graph.add_edge(start_vertex, end_vertex, int(weight))
    return graph

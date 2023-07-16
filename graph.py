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
        visited = set()
        unvisited = list(self.vertices.keys())
        
        while unvisited:
            # Find the vertex with the minimum distance among the unvisited vertices
            current_vertex = min(unvisited, key=lambda vertex: distances[vertex])
            unvisited.remove(current_vertex)
            visited.add(current_vertex)
            
            for neighbor, weight in self.vertices[current_vertex].items():
                if neighbor in unvisited:
                    distance = distances[current_vertex] + weight
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
        
        return distances

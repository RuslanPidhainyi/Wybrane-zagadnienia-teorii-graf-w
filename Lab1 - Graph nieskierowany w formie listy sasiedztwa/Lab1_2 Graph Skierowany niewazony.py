# Graph skierowany w formie listy sąsiedztwa - Graph<Vertex>

class Graph:
    def __init__(self):
        self.dict = {}
    
    def add_vertex(self, vertex):
        if vertex not in  self.dict:
            self.dict[vertex] = []
    
    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.dict[u].append(v)

    def get_neighbors(self, vertex):
        if vertex in self.dict:
            return self.dict[vertex]
        else: 
            return[]
    
    def print_graph(self):
        for vertex, neighbors in self.dict.items():
            print(f"Vertex {vertex}: -> {neighbors}")

g = Graph()
g.add_edge(0,1)
g.add_edge(0,4)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(4,3)

neighbors = g.get_neighbors(1)
print(f"Neighbors of vertex 1 (outgoing edges): {neighbors}")

print("\nDirected graph in the form of an adjacency list:")
g.print_graph()
#Multi-Graph niewazony oraz nieskierowany
class Graph:
    def __init__(self):
        self.dict = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.dict:
            self.dict[vertex] = []
    
    def add_edge(self, u, v,):
        self.add_vertex(u)
        self.add_vertex(v)  
        self.dict[u].append(v)
        self.dict[v].append(u)
    
    def get_neighbors(self, vertex):
        if vertex in self.dict:
            return self.dict[vertex]
        else:
            return []
    
    def print_graph(self):
        print("vertex - neighbors")
        for vertex, neighbors in self.dict.items():
            print(f"{vertex} : {neighbors}")


g = Graph()
g.add_edge(0,1)
g.add_edge(0,1)
g.add_edge(0,4)
g.add_edge(0,4)
g.add_edge(0,4)
g.add_edge(1,2)
g.add_edge(1,4)

neighbors = g.get_neighbors(0)
print(f"Neighbors of vertex 0: {neighbors}")

print()

g.print_graph()

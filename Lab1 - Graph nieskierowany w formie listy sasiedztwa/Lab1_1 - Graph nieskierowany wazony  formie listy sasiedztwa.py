#Graph nieskierowany wazony  formie listy sasiedztwa

#{vertex[a] -> [b(2),c(3)]}
#{vertex[b] -> [a(2)]}
#{vertex[c] -> [a(3)]}
class Graph:
    def __init__(self):
        self.dict = {}

    def add_vertex(self, vertex):
        if vertex not in self.dict:
            self.dict[vertex] = []

    def add_edge(self, u, v, weight):
        self.add_vertex(u)
        self.add_vertex(v)
        self.dict[u].append((v, weight))
        self.dict[v].append((u, weight))
    
    def get_neighbors(self, vertex):
        if vertex in self.dict:
            return self.dict[vertex]
        else:
            return []
        
    def print_graph(self):
        print("Graph in the form of an adjacency list: ")
        
        print() 

        print("Vertex - Neighbors  (Weight of edgees)")

        for vertex, neighbors in self.dict.items():
            print(f"Vertex {vertex}:", end=" ")
            for neighbor, weight in neighbors:
                print(f"{neighbor}({weight})", end=" ")
            print()

g = Graph()
g.add_edge(0, 1, 5) # Додаємо ребро між вершинами 0 та 1 з вагою 5
g.add_edge(0, 4, 3) 
g.add_edge(1, 2, 2)

neighbors = g.get_neighbors(0)
print(f"Neighbors of 0: {neighbors}")

print()

g.print_graph()
class Graph:
    def __init__(self):
        self.dict = {}

    def add_vertex(self, vertex):
        if vertex not in self.dict:
            self.dict[vertex] = []

    def add_edge(self, u, v, weight):
        self.add_vertex(u)
        self.add_vertex(v)
        self.dict[u].append((v, weight)) # Dodajemy skierowane połączenie od u do v z wagą

    def get_neighbors(self, vertex):
        if vertex in self.dict:
            return self.dict[vertex]
        else:
            return []

    def print_graph(self):
        print("Vertex -> Neighbors  (Weight of edgees)")
        for vertex, neighbors in self.dict.items():
            print(f"Vertex {vertex}: -> ", end="")
            neighbor_strings = [f"({neighbor}, {weight})" for neighbor, weight in neighbors]
            print(", ".join(neighbor_strings))


g = Graph()
g.add_edge(0, 1, 5)
g.add_edge(0, 4, 3)
g.add_edge(1, 2, 2)
g.add_edge(4, 3, 1)

neigbors = g.get_neighbors(0)
print(f"Neighbors of 0: {neigbors}")

print()

g.print_graph()
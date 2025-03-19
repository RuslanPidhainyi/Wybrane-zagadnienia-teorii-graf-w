#self   - себе | siebie
#vertex - вершина | wierzchołek
#edge   - ребро | krawędź
#append - додати | dodać


# Python - C#
# : = {} - open & close block of code
# 
# Example with Class:
# 
# C#:
# Class Graph 
# {
#   ...
# } 
#
# Python:
# Class Graph : 
#   ...
# 
#


# Структури Py. | C#                     -          Приклад створення (Python)
#
# List | List<T> або Array в C#                     my_list = [] | my_list = list()
# Dictionary | Dictionary<TKey, TValue> в C#        my_dict = {} | my_dict = dict()
# Queue | Queue<T> в C#                             from queue import Queue; my_queue = Queue()
# Stack | Stack<T> в C#                             from collections import deque; my_stack = deque()
# Set | HashSet<T> в C#                             my_set = set()
# Tuple | Tuple<T1, T2> в C#                        my_tuple = () | my_tuple = tuple()
# Linked List | LinkedList<T> в C#                  from collections import deque; my_linked_list = deque()
   



#Graph nie skierowany w formie listy sasiedztwa - Graph<Vertex,Edge> - Graph<V,E>

#Wkazywania Klasu Graph
class Graph: 
    #Konstruktor __init__ klasy Graph 
    def __init__(self):
        self.adj_list = {}  # self.adj_list = ... - Dajem nazwe zmennej a trybuta klasy - adj_list 
                            # ... = {} - Oraz przepisujemy do nej pustoj Dictionary
    
    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = [] # Dodaje do Dictionary adj_list nowy klucz z pustym Listem
    
    def add_edge(self, u, v):
        self.add_vertex(u) #add vertex u
        self.add_vertex(v) #add vertex v 
        self.adj_list[u].append(v) #Dodajemy edge pomiedzy virtexem V oraz U, czyli dodajemy V do listy sasiedztwa U
        self.adj_list[v].append(u) #Dodajemy edge pomiedzy virtexem V oraz U, czyli dodajemy U do listy sasiedztwa V

    def get_neighbors(self, vertex):
        if vertex in self.adj_list:
            return self.adj_list[vertex]
        else: 
            return []

    def print_graph(self):
        print("Graph in the form of an adjacency list: ")
        print()
        print("Vertex - Neighbors")
        for vertex, neighbors in self.adj_list.items():
            print(f"Vertex {vertex}:", end=" ")
            for neighbor in neighbors:
                print(f"{neighbor}", end=" ")
            print()

# - ?
g = Graph() #Tworzymy obiekt klasy Graph
g.add_edge(0, 1) #Dodajemy edge pomiedzy virtexem 0 oraz 1
g.add_edge(0, 4) #Dodajemy edge pomiedzy virtexem 0 oraz 4

neighbors = g.get_neighbors(0)
print(f"Neighbors of vertex 0: {neighbors}")

print()

g.print_graph()
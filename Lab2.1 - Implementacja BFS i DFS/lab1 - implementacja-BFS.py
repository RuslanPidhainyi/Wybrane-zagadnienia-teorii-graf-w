v = TypeVar('V', bound = Hashble) #Vertex (generic)
from collections import deque #Queue

def bfs(g: BaseGraph, start: v) -> Iterable[v]:

    odwiedzone = set() #Zbior odwiedzonych wierzchołków
    kolejka = deque([start]) #FIFO

    while kolejka:
        v = kolejka.popleft() #Pobierz pierwszy element z kolejki
        
        if v not in odwiedzone:
            yield v             #Zwróć wierzchołek
            odwiedzone.add(v)   #Oznacz wierzchołek jako odwiedzony
            kolejka.extend(u for u in g.neighbors(v) if u not in odwiedzone) #Dodaj sąsiadów do kolejki

g = SimpleGraph() #Tworzenie grafu prosty (nieskierowany, nie zabiera pętli)
                   #ani wielokrotnych krawędzi, niewazony
g.add_edge_from([(1, 2), (1,3), (2,4), (3,5)]) #Dodawanie krawędzi

print(list(bfs(g, 1))) #Wywołanie funkcji BFS i wypisanie wyniku

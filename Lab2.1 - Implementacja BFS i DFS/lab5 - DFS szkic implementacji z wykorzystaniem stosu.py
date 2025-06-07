def dfs_stack(g: BaseGraph, start: V) -> Iterable[V]:

    odwiedzone = set()  # Zbior odwiedzonych wierzchołków
    stos = [start]  #LIFO

    while stos:
        v = stos.pop()
        
        if v not in odwiedzone:
            yield v # Zwróć wierzchołek
            odwiedzone.add(v) #oznacz wierzchołek jako odwiedzony
            stos.extend(u for u in g.neighbors(v) if u not in odwiedzone) #Dodaj sąsiadów do stosu


g = SimpleGraph()  #grafu prosty (nieskierowany, nie zabiera pętli)
#                     # ani wielokrotnych krawędzi, niewazony
g.add_edge_from([(1, 2), (1,3), (2,4), (3,5)]) #Dodawanie krawędzi
print(list(dfs_stack(g, 1))) #Wywołanie funkcji DFS i wypisanie wyniku
# Output: [1, 2, 4, 3, 5]

def dfs(g: BaseGraph, start: V) -> Iterable[V]:

    odwiedzone = set()  # Zbior odwiedzonych wierzchołków
    def dfs_recursive(v):
        if v not in odwiedzone:
            yield v # Zwróć wierzchołek
            odwiedzone.add(v) #oznacz wierzchołek jako odwiedzony
            for u in g.neighbors(v):
                yield from dfs_recursive(u) # Rekurencyjne wywołanie dla sąsiadów

    yield from dfs_recursive(start)  # Wywołanie funkcji rekurencyjnej DFS

g = SimpleGraph()  #grafu prosty (nieskierowany, nie zabiera pętli)
#                     # ani wielokrotnych krawędzi, niewazony
g.add_edge_from([(1, 2), (1,3), (2,4), (3,5)]) #Dodawanie krawędzi
print(list(dfs(g, 1))) #Wywołanie funkcji DFS i wypisanie wyniku
# Output: [1, 2, 4, 3, 5]

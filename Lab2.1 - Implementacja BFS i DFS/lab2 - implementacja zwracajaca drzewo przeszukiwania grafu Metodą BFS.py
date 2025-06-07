from collections import deque


def bfs_tree(g: BaseGraph, start: v) -> Dict[v,v]:

    odwiedzone = set() #Zbior odwiedzonych wezłow
    kolejka = deque([start]) #FIFO
    drzewo = {start: None} #Drzewo przeszukiwania grafu

    while kolejka:
        v = kolejka.popleft() #Pobierz wierzchołek z przodu kolejki
        if v not in odwiedzone:
            odwiedzone.add(v) #Oznacz wierzchołek jako odwiedzony
            for u in g.neighbors(v): 
                if u not in odwiedzone:
                    drzewo[u] = v #Dodaj wierzchołek do drzewa przeszukiwania
                    kolejka.append(u) #Dodaj wezel do kolejki
    
    return drzewo #Zwróć drzewo przeszukiwania grafu

g = SimpleGraph() #graf prosty (nieskierowany, nie zabiera pętli)
                    # ani wielokrotnych krawędzi, niewazony
g.add_edge_from([(1, 2), (1,3), (2,4), (3,5)]) #Dodawanie krawędzi
print(bfs_tree(g, 1)) #Wywołanie funkcji BFS i wypisanie wyniku
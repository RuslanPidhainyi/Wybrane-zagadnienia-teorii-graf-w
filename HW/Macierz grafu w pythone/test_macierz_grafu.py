from macierz_grafu import MacierzGrafu

def main():
    graf = MacierzGrafu(5)
    graf.add_edge(1, 2, 'out')
    graf.add_edge(1, 3, 'in')
    graf.add_edge(1, 5, 'in')
    graf.add_edge(2, 4, 'out')
    graf.add_edge(2, 5, 'out')
    graf.add_edge(3, 1, 'out')
    graf.add_edge(4, 3, 'out')
    graf.add_edge(5, 1, 'out')
    graf.add_edge(5, 4, 'out')

    graf.print_matrix()

    print("Poprzednicy 1:", graf.get_predecessors(1))
    print("Następcy 1:", graf.get_successors(1))

if __name__ == "__main__":
    main()

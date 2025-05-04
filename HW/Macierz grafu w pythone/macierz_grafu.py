class MacierzGrafu:
    def __init__(self, num_vertices):
        self.V = num_vertices
        self.size = self.V + 2
        self.matrix = [[0 for _ in range(self.size)] for _ in range(self.size)]
        
        # Ініціалізація всіх комірок як -j (неінцидентні)
        for i in range(1, self.V + 1):
            for j in range(1, self.V + 1):
                self.matrix[i][j] = -j

    def add_edge(self, from_v, to_v, direction):
        if direction == 'in':
            self._add_predecessor(from_v, to_v)
        elif direction == 'out':
            self._add_successor(from_v, to_v)
        else:
            raise ValueError("direction must be 'in' or 'out'")
    
    def _add_predecessor(self, i, pred):
        if self.matrix[i][0] == 0:  # якщо список пустий
            self.matrix[i][0] = pred
        else:
            last_pred = self.matrix[0][i]
            self.matrix[i][last_pred] = pred
        self.matrix[0][i] = pred
        self.matrix[i][pred] = pred  # адреса → на себе (якщо єдиний або кінець)

    def _add_successor(self, i, succ):
        addr = succ + self.V  # за статтею → зсунути індекс
        if self.matrix[i][self.V + 1] == 0:  # якщо список пустий
            self.matrix[i][self.V + 1] = succ
        else:
            last_succ = self.matrix[self.V + 1][i]
            self.matrix[i][last_succ] = addr
        self.matrix[self.V + 1][i] = succ
        self.matrix[i][succ] = addr  # адреса → на себе (якщо єдиний або кінець)

    def print_matrix(self):
        for row in self.matrix:
            print('\t'.join(f"{x:4}" for x in row))

    def get_predecessors(self, vertex):
        preds = []
        curr = self.matrix[vertex][0]
        while curr != 0:
            preds.append(curr)
            if curr == self.matrix[0][vertex]:
                break
            curr = self.matrix[vertex][curr]
        return preds

    def get_successors(self, vertex):
        succs = []
        curr = self.matrix[vertex][self.V + 1]
        while curr != 0:
            succs.append(curr)
            next_addr = self.matrix[vertex][curr]
            if next_addr >= self.V + 1:
                curr = next_addr - self.V
            else:
                break
        return succs
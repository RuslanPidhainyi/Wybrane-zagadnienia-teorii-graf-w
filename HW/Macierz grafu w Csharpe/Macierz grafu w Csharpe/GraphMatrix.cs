namespace Macierz_grafu_w_Csharpe
{
    //Vertex / Werszawki / Вершина (Кулькі) - це елемент графу, що представляє собою точку з'єднання або вузол у графі. Вершини можуть бути з'єднані ребрами, які представляють зв'язки між ними. У контексті графів, вершини можуть мати різні властивості та атрибути, такі як назва, вага або інші характеристики.
    //Edge / Krawedz / Ребро - це зв'язок між двома вершинами в графі. Ребра можуть бути орієнтованими або неорієнтованими, залежно від того, чи мають вони напрямок. У контексті графів, ребра можуть також мати вагу або інші атрибути, які визначають їх характеристики.
    public class GraphMatrix : IGraphMatrix
    {
        private int[,] _matrix;
        private int _vertexCount;
        private int _size; //фактичний розмір матриці: V + 2.


        /*
         Ініціалізація матриця V+2 x V+2.

            всі клітинки[i, j] між вершинами ініціалізуються як -j
            → це означає, що немає ребра від i до j.

            (-j) = спеціальне значення, що кодує відсутність інцидентності → використовується для зберігання “списку неінцидентних” вершин.
        */

        public GraphMatrix(int numVertices)
        {
            _vertexCount = numVertices;

            //Werszawkuł / Vertex 5 + 2 = 7
            _size = _vertexCount + 2; //фактичний розмір матриці: V + 2. ->  за статтею потрібні додаткові рядки/стовпці для зберігання перших/останніх попередників та наступників. Werszawkuł/Vertex 5 + 2 = 7

            _matrix = new int[_size, _size];

            for (int i = 1; i <= _vertexCount; i++)
            {
                for (int j = 1; j <= _vertexCount; j++)
                {
                    _matrix[i, j] = -j;
                }
            }
        }

        public void AddEdge(int from, int to, string direction)
        {
            if (direction == "in") _AddPrevious(from, to); //якщо ребро входить → додає попередника
            else if (direction == "out") _AddNext(from, to); //якщо виходить → додає наступника
            else throw new ArgumentException("direction must be 'in' or 'out'");
        }

        /*
         * _AddPrevious:
         
         _matrix[i, 0] – вказівник на першого попередника вершини i.

        _matrix[0, i] – вказівник на останнього попередника вершини i.

        _matrix[i, pred] – “адресація” → вказує, хто наступний у списку попередників.
         */
        private void _AddPrevious(int i, int pred)
        {
            //якщо попередників ще немає → просто ставимо pred як першого
            if (_matrix[i, 0] == 0) _matrix[i, 0] = pred;

            /*
             якщо вже є попередник:
                через _matrix[0, i] дізнаємось, хто був останній
                з'єднуємо старий останній → новий
             */
            else
            {
                int lastPred = _matrix[0, i];
                _matrix[i, lastPred] = pred;
            }

            _matrix[0, i] = pred; //оновлюємо останнього попередника → pred
            _matrix[i, pred] = pred; //записуємо адресу нового в _matrix[i, pred]
        }


        /*
         * _AddNext:
         
          addr = succ + V – тут адреса наступника кодується +V, щоб відрізняти від попередників  

          _matrix[i, V+1] – перший наступник

          _matrix[V+1, i] – останній наступник
        
          _matrix[i, succ] – адреса наступного
        */
        private void _AddNext(int i, int succ)
        {
            int addr = succ + _vertexCount;

            if (_matrix[i, _vertexCount + 1] == 0) _matrix[i, _vertexCount + 1] = succ;
            else
            {
                int lastSucc = _matrix[_vertexCount + 1, i];
                _matrix[i, lastSucc] = addr;
            }

            _matrix[_vertexCount + 1, i] = succ;
            _matrix[i, succ] = addr;
        }


        /*
         Отримання списку попередників:

            починаємо з _matrix[vertex, 0] (перший)

            додаємо curr в список

            переходимо до наступного через _matrix[vertex, curr]

            зупиняємось, коли досягли останнього (_matrix[0, vertex])

            → інакше кажучи, обхід пов'язаного списку, записаного через матрицю.
         */
        public List<int> GetPrevious(int vertex)
        {
            List<int> preds = new List<int>();
            int curr = _matrix[vertex, 0];

            while (curr != 0)
            {
                preds.Add(curr);

                if (curr == _matrix[0, vertex]) break;

                curr = _matrix[vertex, curr];
            }

            return preds;
        }

        /*
         Отримання списку наступників:

            починаємо з _matrix[vertex, V+1]

            додаємо curr

            переходимо через _matrix[vertex, curr]

            адреса “розкодовується” → curr = addr - V

          якщо nextAddr < V+1 → кінець
         */

        public List<int> GetNext(int vertex)
        {
            List<int> nexts = new List<int>();
            int curr = _matrix[vertex, _vertexCount + 1];
            HashSet<int> visited = new HashSet<int>();

            while (curr != 0)
            {
                if (!visited.Add(curr)) break;
                
                nexts.Add(curr);
                int nextAddr = _matrix[vertex, curr];

                if (nextAddr >= _vertexCount + 1) curr = nextAddr - _vertexCount;
                else break;
            }

            return nexts;
        }

        public void PrintMatrix()
        {
            for (int i = 0; i < _size; i++)
            {
                for (int j = 0; j < _size; j++)
                {
                    Console.Write($"{_matrix[i, j],4}");
                }

                Console.WriteLine();
            }

            Console.WriteLine();
        }
    }
}
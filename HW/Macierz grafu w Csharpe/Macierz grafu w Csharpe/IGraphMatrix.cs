using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Macierz_grafu_w_Csharpe
{
    public interface IGraphMatrix
    {
        void AddEdge(int from, int to, string direction);
        List<int> GetPrevious(int vertex);
        List<int> GetNext(int vertex);
        void PrintMatrix();
    }
}

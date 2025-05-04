using Macierz_grafu_w_Csharpe;
using System;
using System.Collections.Generic;

public class Program
{
    static void Main(string[] args)
    {
        GraphMatrix graph = new GraphMatrix(5);
        graph.AddEdge(1, 2, "out");
        graph.AddEdge(1, 3, "in");
        graph.AddEdge(1, 5, "in");
        graph.AddEdge(2, 4, "out");
        graph.AddEdge(2, 5, "out");
        graph.AddEdge(3, 1, "out");
        graph.AddEdge(4, 3, "out");
        graph.AddEdge(5, 1, "out");
        graph.AddEdge(5, 4, "out");

        graph.PrintMatrix();

        Console.WriteLine("Poprzednicy 1: " + string.Join(", ", graph.GetPrevious(1)));
        Console.WriteLine("Następcy 1: " + string.Join(", ", graph.GetNext(1)));
    }
}

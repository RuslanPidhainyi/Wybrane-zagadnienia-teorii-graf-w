using Microsoft.VisualStudio.TestTools.UnitTesting;
using Macierz_grafu_w_Csharpe;
using System.Collections.Generic;

namespace MacierzGrafu.Tests
{
    [TestClass]
    public class GraphMatrixTests
    {
        [TestMethod]
        public void AddEdge_ShouldAddPreviousAndNext()
        {
            // Arrange
            var graph = new GraphMatrix(5);

            // Act
            graph.AddEdge(1, 2, "out"); // 1 -> 2
            graph.AddEdge(1, 3, "in");  // 3 -> 1
            graph.AddEdge(1, 5, "in");  // 5 -> 1

            // Assert
            var previous = graph.GetPrevious(1);
            var next = graph.GetNext(1);

            CollectionAssert.AreEquivalent(new List<int> { 3, 5 }, previous);
            CollectionAssert.AreEquivalent(new List<int> { 2 }, next);
        }

        [TestMethod]
        public void GetPrevious_ShouldReturnEmptyList_WhenNoPrevious()
        {
            var graph = new GraphMatrix(5);
            var previous = graph.GetPrevious(2);
            Assert.AreEqual(0, previous.Count);
        }

        [TestMethod]
        public void GetNext_ShouldReturnEmptyList_WhenNoNext()
        {
            var graph = new GraphMatrix(5);
            var next = graph.GetNext(4);
            Assert.AreEqual(0, next.Count);
        }

        [TestMethod]
        public void PrintMatrix_ShouldNotThrowException()
        {
            var graph = new GraphMatrix(5);
            graph.AddEdge(1, 2, "out");
            graph.AddEdge(2, 3, "out");
            graph.AddEdge(3, 1, "in");
            graph.AddEdge(5, 1, "in");

            graph.PrintMatrix(); // just ensure no exception
        }
    }
}

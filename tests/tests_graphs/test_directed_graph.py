import unittest
from data_structures.graphs.directed_graph import DirectedGraph  # Replace 'your_module' with the actual file name if needed

class TestDirectedGraph(unittest.TestCase):

    def setUp(self):
        self.graph = DirectedGraph()
        self.graph.add_node("A")
        self.graph.add_node("B")
        self.graph.add_node("C")

    def test_add_edge(self):
        self.graph.add_edge("A", "B", 5)
        self.assertTrue(self.graph.adjacent("A", "B"))
        self.assertFalse(self.graph.adjacent("B", "A"))
        self.assertEqual(self.graph.matrix[self.graph.node_map["A"]][self.graph.node_map["B"]], 5)

    def test_neighbors(self):
        self.graph.add_edge("A", "B")
        self.graph.add_edge("A", "C")
        neighbors = self.graph.neighbors("A")
        self.assertCountEqual(neighbors, ["B", "C"])

    def test_add_node_duplicate(self):
        with self.assertRaises(ValueError):
            self.graph.add_node("A")

    def test_add_edge_invalid_nodes(self):
        with self.assertRaises(IndexError):
            self.graph.add_edge("A", "Z")

    def test_remove_edge(self):
        self.graph.add_edge("B", "C", 3)
        self.graph.remove_edge("B", "C")
        self.assertFalse(self.graph.adjacent("B", "C"))

    def test_remove_node(self):
        self.graph.add_edge("A", "B")
        self.graph.remove_node("B")
        self.assertNotIn("B", self.graph.node_map)
        self.assertEqual(self.graph.size, 2)
        self.assertEqual(len(self.graph.matrix), 2)
        self.assertEqual(len(self.graph.matrix[0]), 2)

    def test_adjacent(self):
        self.graph.add_edge("C", "A", 2)
        self.assertTrue(self.graph.adjacent("C", "A"))
        self.assertFalse(self.graph.adjacent("A", "C"))

    def test_neighbors_after_node_removal(self):
        self.graph.add_edge("A", "B")
        self.graph.remove_node("B")
        self.assertEqual(self.graph.neighbors("A"), [])

    def test_remove_node_invalid(self):
        with self.assertRaises(IndexError):
            self.graph.remove_node("Z")

    def test_neighbors_invalid_node(self):
        with self.assertRaises(IndexError):
            self.graph.neighbors("Z")

    def test_remove_edge_invalid(self):
        with self.assertRaises(IndexError):
            self.graph.remove_edge("X", "Y")


if __name__ == "__main__":
    unittest.main()

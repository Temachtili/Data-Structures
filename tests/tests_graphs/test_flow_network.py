import unittest
from data_structures.graphs.flow_network import FlowNetwork  # Replace with actual file name if needed

class TestFlowNetwork(unittest.TestCase):

    def setUp(self):
        self.fn = FlowNetwork()
        self.fn.add_node("S")
        self.fn.add_node("A")
        self.fn.add_node("T")

    def test_add_node(self):
        self.fn.add_node("B")
        self.assertIn("B", self.fn.node_map)
        self.assertEqual(len(self.fn.capacity), 4)
        self.assertEqual(len(self.fn.flow), 4)

    def test_add_node_duplicate(self):
        with self.assertRaises(ValueError):
            self.fn.add_node("A")

    def test_add_edge(self):
        self.fn.add_edge("S", "A", 10)
        s = self.fn.node_map["S"]
        a = self.fn.node_map["A"]
        self.assertEqual(self.fn.capacity[s][a], 10)
        self.assertEqual(self.fn.flow[s][a], 0)

    def test_add_edge_invalid(self):
        with self.assertRaises(IndexError):
            self.fn.add_edge("S", "Z", 5)

    def test_adjacent_true_false(self):
        self.fn.add_edge("S", "A", 10)
        self.assertTrue(self.fn.adjacent("S", "A"))
        self.assertFalse(self.fn.adjacent("A", "S"))  # Directed

    def test_neighbors(self):
        self.fn.add_edge("S", "A", 5)
        self.fn.add_edge("S", "T", 7)
        neighbors = self.fn.neighbors("S")
        self.assertCountEqual(neighbors, ["A", "T"])

    def test_neighbors_invalid(self):
        with self.assertRaises(IndexError):
            self.fn.neighbors("Z")

    def test_remove_edge(self):
        self.fn.add_edge("S", "A", 8)
        self.fn.remove_edge("S", "A")
        s = self.fn.node_map["S"]
        a = self.fn.node_map["A"]
        self.assertEqual(self.fn.capacity[s][a], 0)
        self.assertEqual(self.fn.flow[s][a], 0)

    def test_remove_edge_invalid(self):
        with self.assertRaises(IndexError):
            self.fn.remove_edge("X", "Y")

    def test_remove_node(self):
        self.fn.add_edge("S", "A", 4)
        self.fn.remove_node("A")
        self.assertNotIn("A", self.fn.node_map)
        self.assertEqual(self.fn.size, 2)
        self.assertEqual(len(self.fn.capacity), 2)
        self.assertEqual(len(self.fn.capacity[0]), 2)

    def test_remove_node_invalid(self):
        with self.assertRaises(IndexError):
            self.fn.remove_node("X")

    def test_set_source_and_sink(self):
        self.fn.set_source("S")
        self.fn.set_sink("T")
        self.assertEqual(self.fn.source, "S")
        self.assertEqual(self.fn.sink, "T")


if __name__ == "__main__":
    unittest.main()

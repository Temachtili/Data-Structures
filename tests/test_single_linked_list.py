import unittest
import io
import sys
from data_structures.single_linked_list import SingleLinkedList

class TestSingleLinkedList(unittest.TestCase):

    def setUp(self):
        """Set up test cases."""
        self.lista = SingleLinkedList()

    def test_append(self):
        """Test add elements at the end of the list."""
        self.lista.append(10)
        self.lista.append(20)
        self.assertEqual(self.lista.search_by_index(0), 10)
        self.assertEqual(self.lista.search_by_index(1), 20)

    def test_prepend(self):
        """Test add element at the top of the list."""
        self.lista.append(20)
        self.lista.prepend(10)
        self.assertEqual(self.lista.search_by_index(0), 10)
        self.assertEqual(self.lista.search_by_index(1), 20)

    def test_insert(self):
        """Test insert an element in specified index"""
        self.lista.append(10)
        self.lista.append(20)
        self.lista.insert(1, 15)
        self.assertEqual(self.lista.search_by_index(1), 15)

    def test_delete(self):
        """Test delete an element by index"""
        self.lista.append(10)
        self.lista.append(20)
        self.lista.append(30)
        self.lista.delete(1)
        self.assertEqual(self.lista.search_by_index(1), 30)  # Deleted element

    def test_search(self):
        """Test search by index."""
        self.lista.append(10)
        self.lista.append(20)
        self.lista.append(30)
        self.assertEqual(self.lista.search_by_index(2), 30)

    def test_index_out_of_range(self):
        """Test index out of range."""
        with self.assertRaises(IndexError):
            self.lista.search_by_index(0)  # Empty list

        self.lista.append(10)
        with self.assertRaises(IndexError):
            self.lista.search_by_index(5)  # Index out of range

    def test_display(self):
        """Test display list"""
        self.lista.append(10)
        self.lista.append(20)
        self.lista.append(30)
        expected_output = "10 -> 20 -> 30"

        captured_output = io.StringIO()
        original_stdout = sys.stdout  # Store original stdout

        try:
            sys.stdout = captured_output
            self.lista.display()
        finally:
            sys.stdout = original_stdout

        self.assertEqual(captured_output.getvalue().strip(), expected_output)


if __name__ == "__main__":
    unittest.main()

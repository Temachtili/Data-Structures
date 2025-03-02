import sys
import unittest
import io

from data_structures.stacks_and_queues.deque import Deque


class TestDeque(unittest.TestCase):
    def setUp(self):
        self.deque = Deque()

    def test_insert_front(self):
        self.deque.insert_front(5)

        self.assertEqual(self.deque.front.data, 5)                      #
        self.assertEqual(self.deque.back.data, 5)                       # Result obtained: OK
        self.assertEqual(self.deque.get_size(), 1)                      #

    def test_insert_front_multiple_elements(self):
        self.deque.insert_front(5)
        self.deque.insert_front(10)
        self.deque.insert_front(15)

        self.assertEqual(self.deque.front.data, 15)                     #
        self.assertEqual(self.deque.back.data, 5)                       # Result obtained: OK
        self.assertEqual(self.deque.get_size(), 3)                      #

    def test_insert_back(self):
        self.deque.insert_back(15)

        self.assertEqual(self.deque.front.data, 15)                     #
        self.assertEqual(self.deque.back.data, 15)                      # Result obtained: OK
        self.assertEqual(self.deque.get_size(), 1)                      #

    def test_insert_back_multiple_element(self):
        self.deque.insert_back(5)
        self.deque.insert_back(10)
        self.deque.insert_back(15)

        self.assertEqual(self.deque.front.data, 5)                      #
        self.assertEqual(self.deque.back.data, 15)                      # Result obtained: OK
        self.assertEqual(self.deque.get_size(), 3)                      #

    def test_remove_front(self):
        self.deque.insert_front(5)
        self.deque.insert_front(10)
        self.deque.insert_back(15)
        self.assertEqual(self.deque.remove_front(), 10)                 # Result obtained: OK

    def test_remove_front_in_empty(self):
        with self.assertRaises(IndexError) as context:
            self.deque.remove_front()
        self.assertEqual(str(context.exception), "Deque is empty")      # Result obtained: OK

    def test_remove_back(self):
        self.deque.insert_front(5)
        self.deque.insert_front(10)
        self.deque.insert_back(15)
        self.assertEqual(self.deque.remove_back(), 15)                  # Result obtained: OK

    def test_remove_back_in_empty(self):
        with self.assertRaises(IndexError) as context:
            self.deque.remove_back()
        self.assertEqual(str(context.exception), "Deque is empty")      # Result obtained: OK

    def test_peek_front(self):
        self.deque.insert_front(5)
        self.deque.insert_front(10)
        self.deque.insert_back(15)
        self.assertEqual(self.deque.peek_front(), 10)                   # Result obtained: OK

    def test_peek_back(self):
        self.deque.insert_front(5)
        self.deque.insert_front(10)
        self.deque.insert_back(15)
        self.assertEqual(self.deque.peek_back(), 15)                    # Result obtained: OK

    def test_is_empty(self):
        self.assertTrue(self.deque.is_empty())                                  # Result obtained: OK

    def test_is_not_empty(self):
        self.deque.insert_back(5)
        self.assertFalse(self.deque.is_empty())                                 # Result obtained: OK

    def test_get_size(self):
        self.deque.insert_front(5)
        self.deque.insert_front(10)
        self.assertEqual(self.deque.get_size(), 2)                      # Result obtained: OK

    def test_clear(self):
        self.deque.insert_front(5)
        self.deque.insert_front(10)
        self.deque.insert_back(15)
        self.deque.clear()
        self.assertTrue(self.deque.is_empty())                                  # Result obtained: OK

    def test_display(self):
        self.deque.insert_front(5)
        self.deque.insert_front(10)
        self.deque.insert_back(15)

        expected_output = "10 <-> 5 <-> 15"
        capture_output = io.StringIO()
        original_stdout = sys.stdout

        try:
            sys.stdout = capture_output
            self.deque.display()
        finally:
            sys.stdout = original_stdout
        self.assertEqual(capture_output.getvalue().strip(), expected_output)    # Result obtained: OK

if __name__ == '__main__':
    unittest.main()

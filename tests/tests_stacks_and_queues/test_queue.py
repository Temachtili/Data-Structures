import sys
import unittest
import io
from data_structures.stacks_and_queues.queue import Queue

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_enqueue(self):
        self.queue.enqueue(5)
        self.queue.enqueue(10)
        self.assertEqual(self.queue.peek(), 5)
        self.assertEqual(self.queue.rare.data, 10)

    def test_dequeue(self):
        self.queue.enqueue(5)
        self.queue.enqueue(10)
        self.queue.dequeue()
        self.assertEqual(self.queue.peek(), 10)

    def test_dequeue_empty(self):
        with self.assertRaises(IndexError) as context:
            self.queue.dequeue()
        self.assertEqual(str(context.exception), "Queue is empty")

    def test_peek(self):
        self.queue.enqueue(5)
        self.queue.enqueue(10)
        self.assertEqual(self.queue.peek(), 5)

    def test_peek_empty(self):
        with self.assertRaises(IndexError) as context:
            self.queue.peek()
        self.assertEqual(str(context.exception), "Queue is empty")

    def test_empty(self):
        self.assertEqual(self.queue.get_size(), 0)

    def test_not_empty(self):
        self.queue.enqueue(10)
        self.assertEqual(self.queue.get_size(), 1)

    def test_get_size(self):
        self.queue.enqueue(5)
        self.queue.enqueue(10)
        self.assertEqual(self.queue.get_size(), 2)

    def test_display(self):
        self.queue.enqueue(5)
        self.queue.enqueue(10)
        self.queue.enqueue(15)
        expected_output = "5 <- 10 <- 15"

        capture_output = io.StringIO()
        original_stdout = sys.stdout

        try:
            sys.stdout = capture_output
            self.queue.display()
        finally:
            sys.stdout = original_stdout

        self.assertEqual(capture_output.getvalue().strip(), expected_output)

if __name__ == '__main__':
    unittest.main()

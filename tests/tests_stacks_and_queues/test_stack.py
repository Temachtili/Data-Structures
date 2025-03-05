import unittest
from data_structures.stacks_and_queues.stack import Stack  # Assuming the Stack class is in stack.py

class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.get_size(), 3)
        self.assertEqual(self.stack.peek(), 3)

    def test_pop(self):
        self.stack.push('A')
        self.stack.push('B')
        self.stack.push('C')
        self.assertEqual(self.stack.pop(), 'C')
        self.assertEqual(self.stack.pop(), 'B')
        self.assertEqual(self.stack.pop(), 'A')
        self.assertEqual(self.stack.get_size(), 0)
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_peek(self):
        self.stack.push('X')
        self.assertEqual(self.stack.peek(), 'X')
        self.stack.push('Y')
        self.assertEqual(self.stack.peek(), 'Y')
        self.stack.pop()
        self.assertEqual(self.stack.peek(), 'X')
        self.stack.pop()
        with self.assertRaises(IndexError):
            self.stack.peek()

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(10)
        self.assertFalse(self.stack.is_empty())
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())

    def test_get_size(self):
        self.assertEqual(self.stack.get_size(), 0)
        self.stack.push(5)
        self.assertEqual(self.stack.get_size(), 1)
        self.stack.push(15)
        self.assertEqual(self.stack.get_size(), 2)
        self.stack.pop()
        self.assertEqual(self.stack.get_size(), 1)

if __name__ == '__main__':
    unittest.main()

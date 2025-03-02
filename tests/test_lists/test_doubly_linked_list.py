import unittest
from data_structures.lists.doubly_linked_list import DoublyLinkedList

class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.dll = DoublyLinkedList()

    # Test append method
    def test_append(self):
        self.dll.append(10)
        self.dll.append(20)
        self.assertTrue(self.dll.search(10))
        self.assertTrue(self.dll.search(20))

    # Test prepend method
    def test_prepend(self):
        self.dll.prepend(30)
        self.dll.prepend(40)
        self.assertTrue(self.dll.search(30))
        self.assertTrue(self.dll.search(40))

    # Test insert method
    def test_insert(self):
        self.dll.append(50)
        self.dll.append(60)
        self.dll.insert(1, 55)
        self.assertTrue(self.dll.search(55))
        with self.assertRaises(IndexError):
            self.dll.insert(10, 100)

    # Test is_empty method
    def test_is_empty(self):
        self.assertTrue(self.dll.is_empty())
        self.dll.append(70)
        self.assertFalse(self.dll.is_empty())

    # Test remove_front method
    def test_remove_front(self):
        self.dll.append(80)
        self.dll.append(90)
        self.assertEqual(self.dll.remove_front(), 80)
        self.assertEqual(self.dll.remove_front(), 90)
        with self.assertRaises(IndexError):
            self.dll.remove_front()

    # Test remove_back method
    def test_remove_back(self):
        self.dll.append(100)
        self.dll.append(110)
        self.assertEqual(self.dll.remove_back(), 110)
        self.assertEqual(self.dll.remove_back(), 100)
        with self.assertRaises(IndexError):
            self.dll.remove_back()

    # Test remove_at method
    def test_remove_at(self):
        self.dll.append(120)
        self.dll.append(130)
        self.dll.append(140)
        self.assertEqual(self.dll.remove_at(1), 130)
        with self.assertRaises(IndexError):
            self.dll.remove_at(10)

    # Test remove_by_value method
    def test_remove_by_value(self):
        self.dll.append(150)
        self.dll.append(160)
        self.assertTrue(self.dll.remove_by_value(150))
        self.assertFalse(self.dll.remove_by_value(170))

    # Test search method
    def test_search(self):
        self.dll.append(180)
        self.assertTrue(self.dll.search(180))
        self.assertFalse(self.dll.search(190))

    # Test display_forward method
    def test_display_forward(self):
        self.dll.append(200)
        self.dll.append(210)
        self.dll.display_forward()  # Expected output: ['200', '210']

    # Test display_backward method
    def test_display_backward(self):
        self.dll.append(220)
        self.dll.append(230)
        self.dll.display_backward()  # Expected output: ['230', '220']

if __name__ == '__main__':
    unittest.main()

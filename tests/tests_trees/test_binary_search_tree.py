import unittest
from data_structures.trees.binary_search_tree import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):

    def setUp(self):
        """ Sets up a sample BST before each test. """
        self.bst = BinarySearchTree(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.bst.insert(2)
        self.bst.insert(7)
        self.bst.insert(12)
        self.bst.insert(20)

    ## --- INSERTION TESTS --- ##
    def test_insert(self):
        """ Tests if inserting a new node works correctly. """
        self.bst.insert(8)
        self.assertTrue(self.bst.search(8))

    def test_insert_recursive(self):
        """ Tests if recursive insertion works correctly. """
        self.bst.insert_recursive(9)
        self.assertTrue(self.bst.search(9))

    ## --- SEARCH TESTS --- ##
    def test_search_existing_value(self):
        """ Tests searching for an existing value in the BST. """
        self.assertTrue(self.bst.search(7))

    def test_search_non_existing_value(self):
        """ Tests searching for a value that does not exist in the BST. """
        self.assertFalse(self.bst.search(99))

    ## --- MINIMUM AND MAXIMUM TESTS --- ##
    def test_find_min(self):
        """ Tests if `find_min` returns the node with the smallest value. """
        min_node = self.bst.find_min()
        self.assertEqual(min_node.value, 2)

    def test_find_max(self):
        """ Tests if `find_max` returns the largest value in the BST. """
        max_value = self.bst.find_max()
        self.assertEqual(max_value, 20)

    ## --- DELETION TESTS --- ##
    def test_delete_leaf_node(self):
        """ Tests deletion of a leaf node (node with no children). """
        self.bst.delete(2)  # Node with no children
        self.assertFalse(self.bst.search(2))

    def test_delete_node_with_one_child(self):
        """ Tests deletion of a node with one child. """
        self.bst.delete(15)  # Node with one child (20)
        self.assertFalse(self.bst.search(15))
        self.assertTrue(self.bst.search(20))

    def test_delete_node_with_two_children(self):
        """ Tests deletion of a node with two children. """
        self.bst.delete(10)  # Root node with two children
        self.assertFalse(self.bst.search(10))
        self.assertTrue(self.bst.search(12))  # 12 should have replaced 10

    ## --- ERROR HANDLING TESTS --- ##
    def test_find_min_empty_tree(self):
        """ Tests that `find_min` raises an error if the tree is empty. """
        empty_bst = BinarySearchTree()
        with self.assertRaises(IndexError):
            empty_bst.find_min()

    def test_find_max_empty_tree(self):
        """ Tests that `find_max` raises an error if the tree is empty. """
        empty_bst = BinarySearchTree()
        with self.assertRaises(IndexError):
            empty_bst.find_max()

    def test_delete_empty_tree(self):
        """ Tests that `delete` raises an error if the tree is empty. """
        empty_bst = BinarySearchTree()
        with self.assertRaises(IndexError):
            empty_bst.delete(5)

    def test_delete_non_existing_value(self):
        """ Tests that `delete` raises an error when trying to delete a non-existing value. """
        with self.assertRaises(IndexError):
            self.bst.delete(99)

if __name__ == '__main__':
    unittest.main()

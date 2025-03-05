import unittest
from data_structures.trees.binary_tree import BinaryTree, Node
# Import the BinaryTree and Node classes here, assuming they are in the same file or imported properly

class TestBinaryTree(unittest.TestCase):

    def setUp(self):
        # Create a test tree:
        #       1
        #      / \
        #     2   3
        #    / \
        #   4   5
        self.tree = BinaryTree(1)
        self.tree.root.left = Node(2)
        self.tree.root.right = Node(3)
        self.tree.root.left.left = Node(4)
        self.tree.root.left.right = Node(5)

    def test_inorder_traversal(self):
        # Inorder: [4, 2, 5, 1, 3]
        expected = [4, 2, 5, 1, 3]
        result = self.tree.inorder_traversal(self.tree.root)
        self.assertEqual(result, expected)

    def test_preorder_traversal(self):
        # Preorder: [1, 2, 4, 5, 3]
        expected = [1, 2, 4, 5, 3]
        result = self.tree.preorder_traversal(self.tree.root)
        self.assertEqual(result, expected)

    def test_postorder_traversal(self):
        # Postorder: [4, 5, 2, 3, 1]
        expected = [4, 5, 2, 3, 1]
        result = self.tree.postorder_traversal(self.tree.root)
        self.assertEqual(result, expected)

    def test_breadth_first_traversal(self):
        # Breadth-First: [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        result = self.tree.breadth_first_traversal()
        self.assertEqual(result, expected)

    def test_empty_tree(self):
        empty_tree = BinaryTree()  # No argument means an empty tree
        self.assertEqual(empty_tree.inorder_traversal(empty_tree.root), [])
        self.assertEqual(empty_tree.preorder_traversal(empty_tree.root), [])
        self.assertEqual(empty_tree.postorder_traversal(empty_tree.root), [])
        self.assertEqual(empty_tree.breadth_first_traversal(), [])

    def test_single_node_tree(self):
        single_node_tree = BinaryTree(42)
        expected = [42]
        self.assertEqual(single_node_tree.inorder_traversal(single_node_tree.root), expected)
        self.assertEqual(single_node_tree.preorder_traversal(single_node_tree.root), expected)
        self.assertEqual(single_node_tree.postorder_traversal(single_node_tree.root), expected)
        self.assertEqual(single_node_tree.breadth_first_traversal(), expected)

if __name__ == '__main__':
    unittest.main()

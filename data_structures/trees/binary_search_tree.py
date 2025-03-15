#%% md
# # Binary search tree
# *Created by Angel Gael Aviles Gama on python at 03/04/2025*
#%%
### First we need to create our structure Node, which will be the main element in our Binary search tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
#%%
### Now we create our class for the Binary search tree, where all the functions will be contained
class BinarySearchTree:
    def __init__(self, value=None):
        if value is not None:
            self.root = Node(value)
        else:
            self.root = None

    # Function to insert a new node in Tree
    def insert(self, value):
        new_node = Node(value)
        if not self.root:                       # Tree is empty, new node becomes root
            self.root = new_node
            return
        current = self.root
        while current:                          # Search the place for new node
            if value < current.value:               # Left leaf
                if current.left:
                    current = current.left              # Update node to validate
                else:
                    current.left = new_node             # Add new node to left leaf
                    return
            else:                                   # Right leaf
                if current.right:
                    current = current.right             # Update node to validate
                else:
                    current.right = new_node            # Add new node to left leaf
                    return

    # Function to insert a new node in a recursive approach
    def insert_recursive(self, value):
        self.root = self._insert_recursive(self.root, value)    # Starting recursive call with root

    # Recursive function to insert a new node
    def _insert_recursive(self, node, value):
        if not node:                                                # If there is not a new node to validate, return last one
            return Node(value)

        if value < node.value:                                      # Search in left leaf
            node.left = self._insert_recursive(node.left, value)        # Recursive call
        else:                                                       # Search in right leaf
            node.right = self._insert_recursive(node.right, value)      # Recursive call
        return node

    # Function to search a node in a recursive approach
    def search(self, value):
        return self._search_recursive(self.root, value)         # Starting recursive call with root

    # Recursive function to search a node
    def _search_recursive(self, node, value):
        if not node:                                            # If node is null, it means value doesn't exist in Tree
            return False
        if node.value == value:                                 # If value is found
            return True
        if value < node.value:                                  # Search in left leaf
            return self._search_recursive(node.left, value)         # Recursive call
        if value > node.value:                                  # Search in right leaf
            return self._search_recursive(node.right, value)        # Recursive call

    # Function to find min value in tree in a recursive approach
    def find_min(self):
        if not self.root:                           # If tree is empty
            raise IndexError("Empty tree")
        return self._find_min_recursive(self.root)  # Starting recursive call with root

    # Recursive function to find min value in tree
    def _find_min_recursive(self, node):
        if not node.left:                           # If there is no more nodes in left leaf, return last one found
            return node
        return self._find_min_recursive(node.left)  # Recursive call with left node

    # Function to find max value in tree in a recursive approach
    def find_max(self):
        if not self.root:                           # If tree is empty
            raise IndexError("Empty tree")
        return self._find_max_recursive(self.root)  # Starting recursive call with root

    # Recursive function to find max value in tree
    def _find_max_recursive(self, node):
        if not node.right:                          # If there is no more nodes in right leaf, return last one found
            return node.value
        return self._find_max_recursive(node.right) # Recursive call with right node

    # Function to find parent of provided value
    def _search_parent(self, value):
        if not self.root:                                       # Tree is empty
            raise IndexError("Empty tree")
        if self.root.value == value:                            # Root is provided value
            return self.root
        return self._search_parent_recursive(self.root, value)  # Starting recursive call with root

    # Recursive function to find parent of provided value
    def _search_parent_recursive(self, node, value):
        if not node:
            return None
        if (node.left and node.left.value == value) or (node.right and node.right.value == value):  # If node is none or node.value is equals to value
            return node
        if value < node.value:                                      # Search in left side
            return self._search_parent_recursive(node.left, value)      # Recursive call with left node
        if value > node.value:                                      # Search in right side
            return self._search_parent_recursive(node.right, value)     # Recursive call with right node

    # Function to delete a node and replace it with in-order successor
    def delete(self, value):
        if not self.root:                                               # If tree is empty
            raise IndexError("Empty tree")
        if self.root.value == value:                                    # If root is node to delete
            self.root = self._delete_node(self.root)                        # Recursive call with root
            return

        parent_node = self._search_parent(value)
        if not parent_node:                                             # Value is not in tree
            raise IndexError("Value not found")

        # Determine if node to delete is left or right
        if parent_node.left and parent_node.left.value == value:
            parent_node.left = self._delete_node(parent_node.left)          # Recursive call with left side
        elif parent_node.right and parent_node.right.value == value:
            parent_node.right = self._delete_node(parent_node.right)        # Recursive call with right side

    # Function to delete a node and replace it with in-order successor
    def _delete_node(self, node):
        if not node.left and not node.right:                                    # Node without children
            return None

        if not node.left:                                                       # Node with one left child
            return node.right
        if not node.right:                                                      # Node with one right child
            return node.left

        successor = self._find_min_recursive(node.right)                        # Node with two children, find in-order successor
        node.value = successor.value                                            # Replace node value
        node.right = self._delete_node_recursive(node.right, successor.value)   # Delete node

        return node

    # Recursive function to delete node
    def _delete_node_recursive(self, node, value):
        if not node:                                                        # Node doesn't have right child
            return None
        if value < node.value:                                              # Node is not found yet, search in left side
            node.left = self._delete_node_recursive(node.left, value)           # Recursive call with left node
        elif value > node.value:                                            # Node is not found yet, search in right side
            node.right = self._delete_node_recursive(node.right, value)         # Recursive call with right node
        else:                                                               # Node to be deleted was found. Return next node, to maintain tree structure
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
        return node
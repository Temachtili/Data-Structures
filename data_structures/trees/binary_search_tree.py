#%% md
# # Binary tree
# *Created by Angel Gael Aviles Gama on python at 03/02/2025*
#%%
### First we need to create our structure Node, which will be the main element in our Binary tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
#%%
### Now we create our class for the Binary tree, where all the functions will be contained
class BinarySearchTree:
    def __init__(self, value=None):
        if value is not None:
            self.root = Node(value)
        else:
            self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return
        current = self.root
        while current:
            if value < current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = new_node
                    return
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = new_node
                    return

    def insert_recursive(self, value):
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if not node:
            return Node(value)

        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        else:
            node.right = self._insert_recursive(node.right, value)
        return node

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if not node:
            return False
        if node.value == value:
            return True
        if value < node.value:
            return self._search_recursive(node.left, value)
        if value > node.value:
            return self._search_recursive(node.right, value)


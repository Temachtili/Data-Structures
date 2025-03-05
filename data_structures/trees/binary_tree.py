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
class BinaryTree:
    def __init__(self, value=None):
        if value is not None:
            self.root = Node(value)
        else:
            self.root = None

    # Inorder Traversal (Left, Root, Right)
    def inorder_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.inorder_traversal(node.left, result)       # Recursive call to get left side
            result.append(node.value)                       # After add the root
            self.inorder_traversal(node.right, result)      # At the end, recursive call to get right side
        return result

    # Preorder Traversal (Root, Left, Right)
    def preorder_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            result.append(node.value)                       # Start adding the root
            self.preorder_traversal(node.left, result)      # Recursive call to get left side
            self.preorder_traversal(node.right, result)     # At the end, recursive call to get right side
        return result

    # Postorder Traversal (Left, Right, Root)
    def postorder_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.postorder_traversal(node.left, result)     # Recursive call to get left side
            self.postorder_traversal(node.right, result)    # Recursive call to get right side
            result.append(node.value)                       # At the end, add the root
        return result

    def breadth_first_traversal(self):
        if not self.root:
            return []
        result = []
        queue = [self.root]
        temp = 0
        while temp < len(queue):                            # While there are elements in our queue
            current_node = queue[temp]                      # We get the current node (in breadth first order)
            temp += 1
            result.append(current_node.value)               # Adding it to our result

            if current_node.left:
                queue.append(current_node.left)             # Add left elements in our tree
            if current_node.right:
                queue.append(current_node.right)            # Add right elements in our tree

        return result
#%% md
# # Stack
# *Created by Angel Gael Aviles Gama on python at 03/02/2025*
#%%
### First we need to create our structure Node, which will be the main element in our Stack
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
#%%
### Now we create our class for the Stack, where all the functions will be contained (insert_front, remove_front, etc.)
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):           # Add an element to the top of stack
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):                  # Remove the element from the top of the stack, return it
        if self.is_empty():
            raise IndexError("Stack is empty")
        current = self.top
        self.top = current.next
        self.size -= 1
        return current.data

    def peek(self):                 # Retrieve element at top without removing it
        if self.is_empty():
            raise IndexError("Stack is Empty")
        return self.top.data

    def is_empty(self):             # Check if stack is empty
        return self.size == 0

    def get_size(self):             # Retrieve stack size
        return self.size
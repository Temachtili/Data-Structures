#%% md
# # Deque
# *Created by Angel Gael Aviles Gama on python at 03/01/2025*
#%%
### First we need to create our structure Node, which will be the main element in our Deque
from nbformat.v1 import new_notebook


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
#%%
### Now we create our class for the Deque, where all the functions will be contained (insert_front, remove_front, etc.)
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):             # Insert at the end of the list
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def prepend(self, data):            # Insert at the top of the list
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert(self, index, data):      # Insert at specific index
        new_node = Node(data)
        if index == 0:                      # Insert at the beginning
            if not self.head:                   # If list is empty
                self.head = new_node
            else:                               # If not,
                new_node.next = self.head           # update head for the new one and its attributes
                self.head.prev = new_node
                self.head = new_node
            return
        current = self.head
        for _ in range(index-1):            # Through in list in range (index-1). e.g. of for in doubly list:
                                                # [5] <-> [10] <-> [15] <-> [20]; i = 2; range(2-1): for until [5] <-> [10]
            if not current:                     # Check if index is out of range
                raise IndexError("Index out of range")
            current = current.next

        if not current.next:                    # If (index-1) is the last element in list,
            new_node.prev = current                 # just add new element as the new last one
            current.next = new_node
            return

        new_node.prev = current                 # If index is in the middle of the list,
        new_node.next = current.next            # insert new node between current nodes and
        current.next.prev = new_node            # update their attributes
        current.next = new_node

    def is_empty(self):                 # Check if list is empty
        return not self.head

    def remove_front(self):             # Remove first element in list
        if self.is_empty():                 # Check if list is empty
            raise IndexError("List is empty")
        removed_data = self.head.data
        if not self.head.next:              # If there is only one element in list,
            self.head = None                    # set head in None, now list is empty
        else:                               # If not,
            self.head.next.prev = None          # remove prev from second element in list because it becomes in first one
            self.head = self.head.next          # update list head
        return removed_data

    def remove_back(self):
        if self.is_empty():                 # 1. If list is empty
            raise IndexError("List is empty")

        current = self.head
        if not current.next:                # 2. If there is only one element in list
            self.head = None
            return current.data

        while current.next:                 # As long as there is a next element
            current = current.next

        current.prev.next = None            # 3. If there are more than one element in list
        return current.data

    def remove_at(self, index):         # Remove an element by index
        if self.is_empty():                 # 1. If list is empty
            raise IndexError("List is empty")
        current = self.head

        # Case 1: Remove first element in list
        if index == 0:
            if not current.next:                # If there is only one element in list
                self.head = None
            else:                               # If not,
                self.head = current.next            # update head reference to second element
                self.head.prev = None               # remove prev reference of second element
            return current.data

        # Case 2: Removing an element at specific index
        for _ in range(index-1):            # Through in list until range (index-1)
            if not current.next:                # If index is out of range
                raise IndexError("Index out of range")
            current = current.next
        to_remove = current.next
        if not to_remove:                   # Case 3: If index is the size of list
            raise IndexError("Index out of range")

        removed_data = to_remove.data
        if not to_remove.next:              # Case 4: If index is the last element in list
            current.next = None
        else:                               # Case 5: If index is in middle of the list
            to_remove.next.prev = current
            current.next = to_remove.next
        return removed_data

    def remove_by_value(self, data):    # Remove an element by value
        # Case 1: List is empty
        if self.is_empty():
            return False
        current = self.head

        # Case 2: Single element in list
        if not current.next:
            if current.data == data:        # 2.1 Single element match with value
                self.head = None                # List becomes empty
                return True
            else:                           # 2.2 Single element doesn't match, value not found
                return False

        # Case 3: Head match with value in a multiple elements list
        if current.data == data:
            self.head = current.next
            self.head.prev = None
            return True

        # Case 4: Is a multiple elements list
        while current.next:
            if current.data == data:
                current.prev.next = current.next
                current.next.prev = current.prev
                return True
            current = current.next

        # Case 5: Value to delete is the last element in list
        if current.data == data:
            current.prev.next = None
            return True

        return False

    def search(self, data):
        # Case 1: List is empty
        if self.is_empty():
            return False
        current = self.head
        # Case 2 & 3: Single element list / Multiple elements list
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def display_forward(self):          # Display list in a forward approach
        elements = []
        current = self.head
        while current:                      # Through list starting from head to tail
            elements.append(str(current.data))
            current = current.next
        print("Forward: ", elements)

    def display_backward(self):         # Display list in a backward approach
        elements = []
        current = self.head
        while current.next:                 # Through list til current becomes tail
            current = current.next
        while current:                      # Through list starting from tail to head
            elements.append(str(current.data))
            current = current.prev
        print("Backward: ", elements)
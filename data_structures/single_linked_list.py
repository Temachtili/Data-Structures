#%% md
# # Single Linked List
# *Created by Angel Gael Aviles Gama on python at 02/25/2025*
#%%
### First we need to create our structure Node, which will be the main element in our list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
#%%
### Now we create our class for the list, where all the functions will be contained (append, prepend, etc.)
class SingleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):     # At the end of the list
        new_node = Node(data)
        if self.head is None:                       # If head is null
            self.head = new_node                        # means our List is empty
            return
        last_node = self.head
        while last_node.next:                       # Through in the list until last node
            last_node = last_node.next
        last_node.next = new_node                   # Last node doesn't have "next", we assign him our new node

    def prepend(self, data):    # At the top of the list
        new_node = Node(data)
        new_node.next = self.head                   # Current head is our next in new node, if list is empty, next will be None
        self.head = new_node                        # Update head

    def insert(self, index, data):
        if index == 0:                              # If index == 0,
            self.prepend(data)                          # is equals to prepend function, add at the top of the list
            return

        new_node = Node(data)
        current = self.head
        for _ in range(index-1):                    # Through in index - 1 times (e.g. i = 2 then 1 time)
            if not current:
                raise IndexError("Index out of range")
            current = current.next                      # point to the element in current index position
        new_node.next = current                     # Add new node between them,
        current.next = new_node                     # e.g. [5] -> [10] -> [15] -> [20]; insert(2, 19) then [5] -> [10] -> [19] -> [15] -> [20]

    def delete(self, index):
        if not self.head:
            raise IndexError("Empty list")
        if index == 0:                              # If it's the first element,
            self.head = self.head.next                  # just need to replace next reference
            return
        current = self.head
        for _ in range(index-1):                    # Through in index - 1 times (e.g. i = 2 then 1 time)
            if not current:
                raise IndexError("Index out of range")
            current = current.next                      # point to the element in current index position
        if not current.next:                        # Check if index element exists
            raise IndexError("Index out of range")
        current.next = current.next.next            # Replace reference to next element, thus deleting the index element

    def search_by_index(self, index):
        current = self.head
        for _ in range(index):                      # Look for element in range = index
            if not current:
                raise IndexError("Index out of range")
            current = current.next
        if not current:
            raise IndexError("Index out of range")
        return current.data

    def display(self):
        nodes = []
        current = self.head
        while current:                              # As long as there are elements in the List
            nodes.append(str(current.data))
            current = current.next
        print(" -> ".join(nodes))
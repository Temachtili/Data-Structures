#%% md
# # Queue
# *Created by Angel Gael Aviles Gama on python at 02/26/2025*
#%%
### First we need to create our structure Node, which will be the main element in our Queue
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
#%%
### Now we create our class for the Queue, where all the functions will be contained (enqueue, dequeue, etc.)
class Queue:
    def __init__(self):
        self.front = None
        self.rare = None
        self.size = 0

    def enqueue(self, data):    # Add element at the end of the Queue
        new_node = Node(data)
        if not self.front:
            self.front = new_node
        if self.rare:                           # If we currently have a rare
            self.rare.next = new_node               # add next to current rare, creating a new rare
        self.rare = new_node                    # Updating our new rare
        self.size += 1

    def dequeue(self):
        if self.is_empty():                     # Check if Queue is empty
            raise IndexError("Queue is empty")
        dequeued = self.front.data              # Store data to be returned
        self.front = self.front.next            # update front, removing the last one

        if not self.front:                      # Uf Queue becomes empty,
            self.rare = None                        # update rare to None
        self.size -= 1
        return dequeued

    def peek(self):
        if self.is_empty():                     # Check if Queue is empty
            raise IndexError("Queue is empty")
        return self.front.data

    def is_empty(self):
        return not self.front

    def get_size(self):
        return self.size

    def display(self):
        if self.is_empty():                     # Check if Queue is empty
            print("Queue is empty")
            return
        elements = []
        current = self.front
        while current:                          # As long as there are elements in the Queue
            elements.append(str(current.data))
            current = current.next
        print(" <- ".join(elements))
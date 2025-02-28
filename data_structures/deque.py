#%% md
# # Deque
# *Created by Angel Gael Aviles Gama on python at 02/27/2025*
#%%
### First we need to create our structure Node, which will be the main element in our Deque
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
#%%
### Now we create our class for the Deque, where all the functions will be contained (insert_front, remove_front, etc.)
class Deque:
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

    def insert_front(self, data):   # Insert element at the top of the Deque
        new_node = Node(data)
        if not self.front:                  # If Deque is empty,
            self.front = new_node               # now our new node is front and back
            self.back = new_node
        else:                               # If not,
            new_node.next = self.front          # update next in our new node, being the last front,
            self.front.prev = new_node          # update prev from our last front, being our new node
            self.front = new_node               # update front
        self.size += 1                      # Increment size of our Deque

    def insert_back(self, data):    # Insert element at the end of the Deque.
        new_node = Node(data)

        if not self.back:                   # If Deque is empty,
            self.front = new_node               # now our new node is front and back
            self.back = new_node
        else:                               # If not,
            new_node.prev = self.back           # update prev in our new node, being the last back,
            self.back.next = new_node           # update next from our last back, being our new node
            self.back = new_node                # update back
        self.size += 1                      # Increment size of our Deque

    def remove_front(self):         # Remove first element in Deque and return deleted data.
        if not self.front:                  # Check if our Deque is empty
            raise IndexError("Deque is empty")
        removed_data = self.front.data      # Store data to being returned
        self.front = self.front.next        # Remove current front, changing it for the next element in Deque

        if self.front:                      # If Deque don't become empty,
            self.front.next.prev = None         # remove prev from new front, because its prev no longer exists
        else:                               # If yes,
            self.back = None                    # update back to None because now Deque is empty
        self.size -= 1                      # Increment size of our Deque

        return removed_data

    def remove_back(self):          # Remove last element in Deque and return deleted data.
        if self.is_empty():                   # Check if our Deque is empty
            raise IndexError("Deque is empty")
        removed_data = self.back.data       # Store data to being returned
        self.back = self.back.prev          # Remove current back, changing it for the prev element in Deque

        if self.back:                       # If Deque don't become empty,
            self.back.next = None               # remove next from new back, because its next no longer exists
        else:                               # If yes,
            self.front = None                    # update front to None because now Deque is empty
        self.size -= 1                      # Increment size of our Deque

        return removed_data

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def peek_front(self):          # Returns first element without removing it.
        if self.is_empty():                 # Check if our Deque is empty
            raise IndexError("Deque is empty")
        return self.front.data

    def peek_back(self):            # Returns last element without removing it.
        if self.is_empty():                 # Check if our Deque is empty
            raise IndexError("Deque is empty")
        return self.back.data

    def clear(self):                # Clear Deque
        if self.is_empty():                 # Check if our Deque is empty
            raise IndexError("Deque is already clear")
        self.front = None                   #
        self.back = None                    # Change to None all Deque attributes
        self.size = 0                       #

    def display(self):              # Display Deque
        if self.is_empty():                 # Check if our Deque is empty
            raise IndexError("Deque is already clear")
        elements = []
        current = self.front

        while current:                      # As long as there are elements in the Deque
            elements.append(str(current.data))
            current = current.next
        print(" <-> " .join(elements))      # Represent double link in printing
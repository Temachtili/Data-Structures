#%% md
# # Adjacency Matrix
# *Created by Angel Gael Aviles Gama on python at 03/04/2025*
#%%
class DirectedGraph:
    def __init__(self):
        self.size = 0
        self.matrix = []
        self.node_map = {}

    # Add a new node labeled as v
    def add_node(self, v):
        if v in self.node_map:
            raise ValueError("Node already exists")
        self.node_map[v] = self.size
        self.size += 1

        for row in self.matrix:
            row.append(0)
        self.matrix.append([0] * self.size)

    def add_edge(self, u, v, weight=1):
        if u not in self.node_map or v not in self.node_map:
            raise IndexError("One of the nodes does not exist in graph")

        x = self.node_map[u]
        y = self.node_map[v]
        self.matrix[x][y] = weight

    # Return True if u is adjacent to v
    def adjacent(self, u, v):
        if u in self.node_map and v in self.node_map:
            x = self.node_map[u]
            y = self.node_map[v]
            return self.matrix[x][y] != 0
        return False

    # List all adjacent nodes to node v
    def neighbors(self, v):
        if v not in self.node_map:
            raise IndexError("Node does not exist")

        i = self.node_map[v]
        return [key for key, index in self.node_map.items() if self.matrix[i][index] != 0]

    # Remove v node from graph
    def remove_node(self, v):
        if v not in self.node_map:
            raise IndexError("Node does not exist")

        index = self.node_map[v]
        self.matrix.pop(index)

        for row in self.matrix:
            row.pop(index)

        del self.node_map[v]

        for key in self.node_map:
            if self.node_map[key] > index:
                self.node_map[key] -= 1

        self.size -= 1

    # Remove an existing edge between u and v nodes
    def remove_edge(self, u, v):
        if u not in self.node_map or v not in self.node_map:
            raise IndexError("One of the nodes does not exist in graph")

        x = self.node_map[u]
        y = self.node_map[v]

        self.matrix[x][y] = 0

    def display(self):
        labels = list(self.node_map.keys())
        print("   ", "  ".join(labels))
        for label in labels:
            i = self.node_map[label]
            row = [str(self.matrix[i][self.node_map[lab]]) for lab in labels]
            print(label, " ".join(row))

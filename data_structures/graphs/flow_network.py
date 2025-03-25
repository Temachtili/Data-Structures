#%% md
# # Flow Network
# *Created by Angel Gael Aviles Gama on python at 03/25/2025*
#%%
class FlowNetwork:
    def __init__(self):
        self.size = 0
        self.capacity = []
        self.flow = []
        self.node_map = {}
        self.source = None
        self.sink = None

    def set_source(self, label):
        self.source = label

    def set_sink(self, label):
        self.sink = label

    # Add a new node labeled as v
    def add_node(self, v):
        if v not in self.node_map:
            self.node_map[v] = self.size
            self.size += 1

            for row in self.capacity:
                row.append(0)
            self.capacity.append([0] * self.size)

            for row in self.flow:
                row.append(0)
            self.flow.append([0] * self.size)
            return
        raise ValueError("Node already exists")

    def add_edge(self, u, v, cap):
        if u not in self.node_map or v not in self.node_map:
            raise IndexError("One of the nodes does not exist in graph")

        x = self.node_map[u]
        y = self.node_map[v]
        self.capacity[x][y] = cap
        self.flow[x][y] = 0

    # Return True if u is adjacent to v
    def adjacent(self, u, v):
        if u in self.node_map and v in self.node_map:
            x = self.node_map[u]
            y = self.node_map[v]
            return self.capacity[x][y] != 0
        return False

    # List all adjacent nodes to node v
    def neighbors(self, v):
        if v not in self.node_map:
            raise IndexError("Node does not exist")

        i = self.node_map[v]
        return [key for key, index in self.node_map.items() if self.capacity[i][index] != 0]

    # Remove v node from graph
    def remove_node(self, v):
        if v not in self.node_map:
            raise IndexError("Node does not exist")

        index = self.node_map[v]
        self.capacity.pop(index)
        self.flow.pop(index)

        for row in self.capacity:
            row.pop(index)

        for row in self.flow:
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

        self.capacity[x][y] = 0
        self.flow[x][y] = 0

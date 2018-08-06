class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.visited = False
        self.parent = None

    def __repr__(self):
        return "Value: {}, Edges: {}, Visited: {}, Parent: {}".format(self.value, self.edges, self.visited, self.parent)

    def set_edges(self, edges):
        self.edges = edges

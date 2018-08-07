class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.visited = False

    def __repr__(self):
        return "Value: {}, Edges: {}, Visited: {}".format(self.value, self.edges, self.visited)

    def set_edges(self, edges):
        self.edges = edges

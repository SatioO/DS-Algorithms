class Node:
    def __init__(self, value):
        self.value = value
        self.visited = False
        self.parent = None
        self.edges = []

    def __repr__(self):
        return f'Value: {self.value}, Parent: {self.parent}, Visited: {self.visited}, Edges: {self.edges}'

    def set_edges(self, edges):
        self.edges = edges
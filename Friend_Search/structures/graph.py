class Graph:
    def __init__(self):
        self.nodes = []
        self.graph = {}

    def add_node(self, node):
        self.graph[node.value] = node
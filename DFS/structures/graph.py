class Graph:
    def __init__(self):
        self.graph = {}
        self.start = None
        self.end = None

    def get_node(self, value):
        return self.graph[value]

    def add_node(self, node):
        self.graph[node.value] = node

    def set_start(self, value):
        self.start = self.graph[value]
        return self.start

    def set_end(self, value):
        self.end = self.graph[value]
        return self.end

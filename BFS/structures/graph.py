class Graph(object):
    def __init__(self):
        self.nodes = []
        self.graph = {}
        self.start = None
        self.end = None

    def add_node(self, node):
        self.graph[node.value] = node
        self.nodes.append(node)

    def get_node(self, node):
        return self.graph[node]

    def set_start(self, node):
        self.start = self.graph[node]
        return self.start

    def set_end(self, node):
        self.end = self.graph[node]
        return self.end

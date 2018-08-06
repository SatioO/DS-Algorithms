import argparse
import json
from structures import Node, Graph
from collections import deque


def read_file(filename):
    with open(filename) as f:
        return json.loads(f.read())


if __name__ == "__main__":
    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str, default="data/graph.json")
    parser.add_argument("--start", type=int, default=1)
    parser.add_argument("--end", type=int, default=10)
    args = parser.parse_args()

    # read file
    data = read_file(args.data)

    # create a graph
    graph = Graph()

    for vertex in data:
        # create a node
        t = Node(vertex["id"])
        # set edges
        t.set_edges(vertex["edges"])
        # add node to the graph
        graph.add_node(t)

    # start with initial vertex
    start_node = graph.set_start(args.start)
    end_node = graph.set_end(args.end)

    # create queue
    queue = deque()
    queue.append(start_node)

    while len(queue) > 0:
        current_node = queue.popleft()

        if current_node == end_node:
            print("Found: {}".format(current_node.value))
            break

        for i, edge in enumerate(current_node.edges):
            current_edge = graph.get_node(edge)
            if not current_edge.visited:
                current_edge.visited = True
                queue.append(current_edge)

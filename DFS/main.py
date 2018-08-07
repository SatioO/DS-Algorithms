import argparse
import json
import collections
from structures import Node, Graph


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

    stack = []
    done = False

    def iterate(start, end):
        start_node = graph.set_start(start)
        end_node = graph.set_end(end)
        global done

        if start_node == end_node:
            print("Found: {}".format(start_node.value))
            done = True

        if not start_node.visited and not done:

            print(start_node)
            start_node.visited = True

            for edge in start_node.edges:
                iterate(edge, end)

    iterate(args.start, args.end)

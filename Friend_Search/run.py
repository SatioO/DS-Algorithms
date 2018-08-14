import argparse
import json
from structures import Node, Graph
from collections import deque

g = Graph()


def prepare_data(data):
    for node in data:
        n = Node(node['id'])
        n.set_edges(node['edges'])
        g.add_node(n)


def read_file(path):
    with open(path) as f:
        data = json.loads(f.read())
    return data


def BFS(args):
    queue = deque()
    result = {}
    queue.append(g.graph[args.start])
    degree = 0

    while (len(queue) > 0):
        node = queue[0]
        
        if node.visited != True:
            node.visited = True
            
            if node.parent not in result and node.parent is not None:
                result[node.parent] = degree
                degree+=1

            if node.value == args.end:
                result[node.value] = degree
                # print(f'Found: {node}')
                break

            for n in node.edges:
                if g.graph[n].parent == None:
                    g.graph[n].parent = node.value

                queue.append(g.graph[n])

        queue.popleft()

    print(f'{args.end} is a {degree}rd degree connection to {args.start}')


def main(args):
    path = args.data + 'friends.json'
    data = read_file(path)
    prepare_data(data)

    BFS(args)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str, default="data/")
    parser.add_argument("--start", type=str, default=1)
    parser.add_argument("--end", type=str, default=10)
    args = parser.parse_args()
    main(args)
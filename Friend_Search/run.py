import argparse
import json
from collections import deque
from structures import Node, Graph

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
    matched = False

    while (len(queue) > 0):
        node = queue[0]
        
        if node.visited != True:
            node.visited = True
            
            if node.parent not in result and node.parent is not None:
                result[node.parent] = degree
                
                degree+=1

            if node.value == args.end:
                result[node.value] = degree
                matched = True
                print(f'Found: {node}')
                break

            for n in node.edges:
                if g.graph[n].parent == None:
                    g.graph[n].parent = node.value

                queue.append(g.graph[n])

        queue.popleft()

    if matched:
        return degree, result
    else:
        return 0, {}


def main(args):
    data = read_file(args.data)
    prepare_data(data)

    degree, connections = BFS(args)
    print(f'{args.end} is a {degree} degree connection to {args.start}')
    print(connections)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str, default="data/friends.json")
    parser.add_argument("--start", type=str, default="vaibhav-satam")
    parser.add_argument("--end", type=str, default="ronak-shah")
    args = parser.parse_args()
    main(args)
import heapq
from structures import Node
from collections import Counter
from itertools import groupby

data = 'the frog at the bottom of the well drifts off into the great ocean'


def huffman(data: str):
    itemqueue = [Node(a, len(list(b))) for a, b in groupby(sorted(data))]
    heapq.heapify(itemqueue)

    while len(itemqueue) > 1:
        l = heapq.heappop(itemqueue)
        r = heapq.heappop(itemqueue)
        n = Node(None, l.weight + r.weight)
        n.setChild(l, r)
        heapq.heappush(itemqueue, n)

    codes = {}

    def generate_codes(s, node):
        if node.item:
            if not s:
                codes[node.item] = "0"
            else:
                codes[node.item] = s
        else:
            generate_codes(s + "0", node.left)
            generate_codes(s + "1", node.right)

    generate_codes("", itemqueue[0])
    print(codes)


huffman(data)

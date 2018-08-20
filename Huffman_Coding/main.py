#!/usr/bin/env python
# Compresssion: Huffman Coding Example
# Author: Vaibhav Satam <vaibhav.satam29991@gmail.com>

import heapq
from collections import defaultdict, Counter
from typing import Dict

data = 'The frog at the bottom of the well drifts off into the great ocean'


def encode(freq: Dict[str, int]) -> str:
    heap = [[weight, [symbol, '']] for symbol, weight in freq.items()]
    heapq.heapify(heap)
    while (len(heap) > 1):
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)

        for pair in lo[1:]:
            pair[1] = '0' + pair[1]

        for pair in hi[1:]:
            pair[1] = '1' + pair[1]

        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))


frequency = Counter(data)
huff = encode(frequency)
print(huff)

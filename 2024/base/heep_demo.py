from heapq import *
from random import shuffle
data = list(range(10))
shuffle(data)
print(data)
heap = []
for n in data:
    heappush(heap, n)
print(heap)
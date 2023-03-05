import sys
si = sys.stdin.readline
import heapq
n = int(input())
prb = sorted([[*map(int, si().split())]for _ in range(n)])
h = []
for d, v in prb:
  heapq.heappush(h, v)
  while len(h) > d:
    heapq.heappop(h)
print(sum(h))
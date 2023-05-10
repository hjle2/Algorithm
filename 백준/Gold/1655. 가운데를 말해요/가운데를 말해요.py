import heapq
import sys

r = sys.stdin.readline
n = int(r())

lheap = []
rheap = []
answer = []

for i in range(n):
    a = int(r())

    if len(lheap) == len(rheap):
        heapq.heappush(lheap, -a)
    else:
        heapq.heappush(rheap, a)

    if rheap and -lheap[0] > rheap[0]:
        min = heapq.heappop(rheap)
        max = -heapq.heappop(lheap)
        heapq.heappush(lheap, -min)
        heapq.heappush(rheap, max)
    answer.append(-lheap[0])

print(*answer, sep='\n')

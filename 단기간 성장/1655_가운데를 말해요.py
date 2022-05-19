import heapq
import sys

r = sys.stdin.readline
n = int(r())

left_heap = []
right_heap = []
answer = []

for i in range(n):
    a = int(r())

    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -a)
    else:
        heapq.heappush(right_heap, a)

    if right_heap and -left_heap[0] > right_heap[0]:
        min = heapq.heappop(right_heap)
        max = -heapq.heappop(left_heap)
        heapq.heappush(left_heap, -min)
        heapq.heappush(right_heap, max)
    answer.append(-left_heap[0])

print(*answer, sep='\n')

import sys
import heapq
input = sys.stdin.readline

N = int(input())
ST = [[*map(int, input().split())]for _ in range(N)]
ST.sort()

heap = []
heapq.heappush(heap, ST[0][1])

for i in range(1, N):
    if ST[i][0] >= heap[0]:
        heapq.heappop(heap)
    heapq.heappush(heap, ST[i][1])
print(len(heap))
import sys
import heapq
input = sys.stdin.readline
N = int(input())
card = []
for _ in range(N):
    heapq.heappush(card, int(input()))
cnt = 0
while len(card) > 1:
    tmp = heapq.heappop(card) + heapq.heappop(card)
    cnt += tmp
    heapq.heappush(card, tmp)
print(cnt)
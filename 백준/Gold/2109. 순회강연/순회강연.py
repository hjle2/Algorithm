import heapq
import sys
input = sys.stdin.readline
n = int(input())
d_p = []
max_d = 0
for _ in range(n):
    p, d = map(int, input().split())
    d_p.append((d, p))
    max_d = max(max_d, d)
d_p.sort()

ans, idx = 0, n-1
que = []
while max_d > 0:
    while idx >= 0 and d_p[idx][0] >= max_d:
        heapq.heappush(que, -d_p[idx][1])
        idx -= 1
    if que:
        ans -= heapq.heappop(que)
    max_d -= 1
print(ans)
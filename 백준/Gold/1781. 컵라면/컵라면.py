import heapq
import sys
input = sys.stdin.readline
n = int(input())
cup = []
last_deadline = 0
for _ in range(n):
    a, b = map(int, input().split())
    last_deadline = max(last_deadline, a)
    cup.append((a, b))
cup.sort(key=lambda x:(-x[0], -x[1]))

que = []
idx, ans = 0, 0
while last_deadline > 0:
    while idx < n and cup[idx][0] >= last_deadline:
        heapq.heappush(que, -cup[idx][1])
        idx += 1
    last_deadline -= 1
    if que:
        ans -= heapq.heappop(que)
print(ans)

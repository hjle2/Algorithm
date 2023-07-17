import heapq

n, m = map(int, input().split())
ar = [*map(int, input().split())]

ar.sort()
que = []
while ar:
    for _ in range(m):
        if not ar: break
        if len(que) < m:
            heapq.heappush(que, ar.pop())
        else:
            tmp = heapq.heappop(que)
            heapq.heappush(que, tmp + ar.pop())
ans = 0
while que:
    ans = heapq.heappop(que)
print(ans)
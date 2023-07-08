import heapq

n, m = map(int, input().split())
ar = [*map(int, input().split())]

heapq.heapify(ar)
ans = 0
for _ in range(m):
    tmp = heapq.heappop(ar) + heapq.heappop(ar)
    ans += tmp
    heapq.heappush(ar, tmp)
    heapq.heappush(ar, tmp)
print(sum(ar))
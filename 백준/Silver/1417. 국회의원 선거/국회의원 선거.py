import heapq

n = int(input())
k = int(input())
ar = [0]
for _ in range(n-1):
    heapq.heappush(ar, -int(input()))

ans = 0
while -ar[0] >= k:
    tmp = - heapq.heappop(ar)
    k += 1
    heapq.heappush(ar, -tmp+1)
    ans += 1
print(ans)
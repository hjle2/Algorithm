import heapq

for _ in range(int(input())):
    n = int(input())
    ar = [*map(int, input().split())]
    ar.sort()

    ans = 0
    heapq.heapify(ar)
    while len(ar) > 1:
        tmp = heapq.heappop(ar) + heapq.heappop(ar)
        ans += tmp
        heapq.heappush(ar, tmp)
    print(ans)
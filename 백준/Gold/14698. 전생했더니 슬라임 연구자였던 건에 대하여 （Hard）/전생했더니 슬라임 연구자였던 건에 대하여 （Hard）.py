import heapq
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    ar = [*map(int, input().split())]
    heapq.heapify(ar)

    ans = 1
    while len(ar) > 1:
        tmp = heapq.heappop(ar) * heapq.heappop(ar)
        ans *= tmp % 1000000007
        heapq.heappush(ar, tmp)
    print(ans % 1000000007)
import heapq
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
beer =[[*map(int, input().split())]for _ in range(k)]
beer.sort(key=lambda x:(x[1], x[0])) # 선호도, 도수레벨 순 정렬

total, ans = 0, -1
que = []
for i, (v, c) in enumerate(beer):
    heapq.heappush(que, v)
    total += v

    if len(que) > n:
        total -= heapq.heappop(que)

    if len(que) == n and total >= m:
        ans = c
        break
print(ans)
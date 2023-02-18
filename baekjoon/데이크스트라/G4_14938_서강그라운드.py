import heapq
import sys
input = sys.stdin.readline
INF = 1e9

def dijkstra(s):
    d = [INF] * N
    d[s] = 0
    q = [(0, s)]
    while q:
        w, cur = heapq.heappop(q)
        for nxt, wei in edge[cur]:
            if d[nxt] > w + wei:
                d[nxt] = w + wei
                heapq.heappush(q, (d[nxt], nxt))
    return d


N, M, R = map(int, input().split())
T = [*map(int, input().split())]
edge = [[]for _ in range(N)]
for _ in range(R):
    a, b, l = map(int, input().split())
    edge[a-1].append((b-1, l))
    edge[b-1].append((a-1, l))

ans = 0
for k in range(N):
    item = 0
    for i, dist in enumerate(dijkstra(k)):
        if dist <= M:
            item += T[i]
    ans = max(ans, item)
print(ans)
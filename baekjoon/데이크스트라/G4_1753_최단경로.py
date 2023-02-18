import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):
    q = [(0, start)]
    d[start] = 0
    while q:
        wei, v = heapq.heappop(q)
        if d[v] < wei: continue
        for w, u in edge[v]:
            if w + wei < d[u]:
                d[u] = wei + w
                heapq.heappush(q, (d[u], u))
    for i in range(V):
        print(d[i] if d[i] < INF else 'INF')

INF = 1e9
V, E = map(int, input().split())
K = int(input()) - 1
edge = [[]for _ in range(V)]
for _ in range(E):
    u, v, w = map(int, input().split())
    edge[u-1].append((w, v-1))
d = [INF] * V
dijkstra(K)
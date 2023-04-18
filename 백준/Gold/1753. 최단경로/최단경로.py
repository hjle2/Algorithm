import heapq
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input()) # 시작 정점

graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# u, v, w u->v 가중치 w

def dijkstra(s):
    d = [1e9] * (v+1)
    d[s] = 0
    que = [(0, s)]
    while que:
        weight, vertex = heapq.heappop(que)

        if d[vertex] < weight:
            continue

        for nxt, wei in graph[vertex]:
            tmp_w = weight + wei
            if tmp_w < d[nxt]:
                d[nxt] = tmp_w
                heapq.heappush(que, (tmp_w, nxt))
    return d[1:]


ans = dijkstra(k)
for i in ans:
    if i == 1e9:
        print('INF')
    else:
        print(i)


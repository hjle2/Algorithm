# 방향성이 없는 그래프
# 1에서 N 으로 최단 거리로 이동
# 임의의 주어진 두 정점은 반드시 통과해야 함
# 이동했던 정점, 간선 이동 가능
import heapq
import sys

def dijkstra(start):
    d = [INF] * N
    d[start] = 0
    q = [(0, start)]
    while q:
        dist, cur = heapq.heappop(q)
        for i in range(N):
            if graph[cur][i] < INF and graph[cur][i] + dist < d[i]:
                d[i] = graph[cur][i] + dist
                heapq.heappush(q, (d[i], i))
    return d


input = sys.stdin.readline
INF = 1e9
N, E = map(int, input().split())
graph = [[INF] * N for _ in range(N)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = c
    graph[b-1][a-1] = c
U, V = map(int, input().split())

D = dijkstra(0)
D2 = dijkstra(U-1)[V-1]
D3 = dijkstra(N-1)
ans = D[U-1] + D2 + D3[V-1]
ans = min(ans, D[V-1] + D2 + D3[U-1])
print(ans if ans < INF else -1)
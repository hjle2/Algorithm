# g, h를 지나는 최단 거리의 dest를 구한다.
import heapq
import sys

input = sys.stdin.readline


# s에서 시작하여 다른 노드까지의 최단 거리를 구한다
def dijkstra(s):
    d = [1e9] * (n+1)
    d[s] = 0
    que = [(0, s)]
    while que:
        weight, cur = heapq.heappop(que)
        if d[cur] < weight: continue

        for nxt, wei in graph[cur]:
            if d[nxt] > weight + wei:
                d[nxt] = weight + wei
                heapq.heappush(que, (d[nxt], nxt))
    return d


for _ in range(int(input())):
    n, m, t = map(int, input().split())     # 교차로, 도로, 목적지 후보의 개수
    s, g, h = map(int, input().split())     # 예술가들의 출발지, 후각으로 알아낸 듀오가 지나간 도로

    graph = [[] for _ in range(n+1)]
    for i in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))
    dest = []
    for i in range(t):
        dest.append(int(input()))

    d = dijkstra(s)                       # 시작점 s에서 모든 노드까지의 최단 거리
    dg, dh = dijkstra(g), dijkstra(h)   # g, h에서 시작했을 때 다른 노드까지의 거리

    ans = []
    for dd in dest:
        if d[dd] == d[g] + dg[h] + dh[dd] or d[dd] == d[h] + dh[g] + dg[dd]:
            ans.append(dd)
    ans.sort()
    print(*ans)



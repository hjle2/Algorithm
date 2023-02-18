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
        if d[cur] < w: continue
        for nxt, wei in road[cur]:
            if d[nxt] > w + wei:
                d[nxt] = w + wei
                heapq.heappush(q, (d[nxt], nxt))
    return d

for _ in range(int(input())):
    N, M, T = map(int, input().split())
    S, G, H = map(int, input().split())
    road = [[]for _ in range(N)]
    gh = 0
    for _ in range(M):
        a, b, d = map(int, input().split())
        road[a-1].append((b-1, d))
        road[b-1].append((a-1, d))
        if (a == G and b == H) or (a == H and b == G):
            gh = d
    dest = []
    for _ in range(T):
        dest.append(int(input())-1)
    d = dijkstra(S-1)
    g, h = d[G-1] + gh, d[H-1] + gh
    dg, dh = dijkstra(H-1), dijkstra(G-1)
    ans = []
    for des in dest:
        if d[des] < g + dg[des] and d[des] < h + dh[des]:
            continue
        ans.append(des+1)
    print(*sorted(ans), sep=' ')



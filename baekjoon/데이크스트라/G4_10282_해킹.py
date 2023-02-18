import heapq
import sys
input = sys.stdin.readline
INF = 1e9
def dijkstra(s):
    d = [INF] * N
    d[s] = 0
    q = [(0, s)]
    while q:
        t, cur = heapq.heappop(q)
        for nxt, time in net[cur]:
            if d[nxt] > t + time:
                d[nxt] = t + time
                heapq.heappush(q, (d[nxt], nxt))
    ans1, ans2 = 0, 0
    for i in range(N):
        if d[i] == INF:
            continue
        ans1+=1
        ans2 = max(ans2, d[i])
    print(ans1, ans2)


for _ in range(int(input())):
    N, D, C = map(int, input().split())
    net = [[]for _ in range(N)]
    for _ in range(D):
        a, b, s = map(int, input().split())
        net[b-1].append((a-1, s))
    dijkstra(C-1)

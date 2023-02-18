import heapq
import sys
def dijkstra(frm):
    d[frm] = 0
    q = [(0, frm)]
    while q:
        fare, cur = heapq.heappop(q)
        if fare > d[cur]: continue
        for nxt, w in bus[cur]:
            if w + fare < d[nxt]:
                d[nxt] = w + fare
                heapq.heappush(q, (d[nxt], nxt))


r = sys.stdin.readline
N = int(r())
M = int(r())
bus = [[]for _ in range(N)]
for _ in range(M):
    frm, to, fare = map(int, r().split())
    bus[frm-1].append((to-1, fare))
frm, to = map(int, r().split())
d = [1e9] * N
dijkstra(frm-1)
print(d[to-1])

# N개의 마을에 한명의 학생이 산다
# X 마을에 모여 파티를 벌인다
# M 개의 단방향 도로가 있고, i번째 길을 지나는데 Ti시간이 걸린다
# 학생들은 파티에 참석하기 위해 최단 방향으로 걸어가서 다시 그들의 마을로 돌아온다
# N 명의 학생 중 오고 가는데 가장 많은 시간을 소비하는 학생을 구하라
import heapq
import sys

def dijkstra(start, end):
    d = [1e9] * N
    d[start] = 0
    q = [(0, start)]
    while q:
        total, now = heapq.heappop(q)
        if d[now] < total: continue
        for nxt, t in road[now]:
            if d[nxt] > t + total:
                d[nxt] = t + total
                heapq.heappush(q, (d[nxt], nxt))
    return d[end]

r = sys.stdin.readline
N, M, X = map(int, r().split())
road = [[]for _ in range(N)]
for _ in range(M):
    frm ,to, t = map(int, r().split())
    road[frm-1].append((to-1, t))
ans = 0
for i in range(N):
    ans = max(ans, dijkstra(i, X-1) + dijkstra(X-1, i))
print(ans)
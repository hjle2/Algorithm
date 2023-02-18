# 모든 도로의 거리는 1
# N개의 도시, M개의 단방향 도로
# 특정 도시 X에서 출발하여 도달할 수 있는 도시 중 최단 거리가 정확히 K인 모든 도시를 번호 순으로 출력
import heapq
import sys

input = sys.stdin.readline
from collections import deque
def getKDistance():
    ans = []
    for i in range(N):
        if d[i] == K: ans.append(i+1)
    return ans

def getSmallIndex():
    mind = 1e9
    idx = 0
    for i in range(N):
        if d[i] < mind and not v[i]:
            mind, idx = d[i], i
    return idx

# 시간 초과 input 을 sys.stdin.readline 으로 바꿔주니 통과 됨!!
# def dijkstra(X):
#     # 인접 정점의 거리 계산
#     for u in edge[X]:
#         d[u] = 1
#     # 시작 정점의 방문 처리, 거리 초기화
#     v[X] = 1
#     d[X] = 0
#     for i in range(N):
#         cur = getSmallIndex()
#         v[cur] = 1
#         for u in edge[cur]:
#             if v[u]: continue
#             if d[cur] + 1 < d[u]:
#                 d[u] = d[cur] + 1

def dijkstra(start):
    d[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        cur_d, cur = heapq.heappop(q)
        if d[cur] < cur_d: continue
        for u in edge[cur]:
            if cur_d + 1 < d[u]:
                d[u] = cur_d + 1
                heapq.heappush(q, (d[u],u))


N, M, K, X = map(int, input().split())
edge = [[]for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    edge[a-1].append(b-1)
d = [1e9] * N
v = [0] * N
dijkstra(X-1)
ans = []
for i in range(N):
    if d[i] == K: ans.append(i + 1)
if ans: print(*ans, sep='\n')
else: print(-1)
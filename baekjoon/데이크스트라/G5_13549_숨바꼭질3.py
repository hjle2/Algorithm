# 수빈이의 위치 N, 동생의 위치 K
# 수빈이는 현재의 위치 X에서 X-1, X+1로 이동 가능
# 순간이동하면 0초 후 2*X 로 이동
# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간을 구하라
import heapq
from collections import deque
def dijkstra():
    q = [(0, N)]
    d[N] = 0
    while q:
        t, cur = heapq.heappop(q)
        if cur >= len(d) or t > d[cur]: continue
        for nxt in [cur+1, cur-1]:
            if 0 <= nxt < len(d) and d[nxt] > t+1:
                d[nxt] = t+1
                heapq.heappush(q, (t+1, nxt))
        if cur*2 < len(d) and d[cur*2] > t:
            d[cur*2] = t
            heapq.heappush(q, (t, cur*2))
    return d[K]


def bfs():
    q = deque([N])
    d[N] = 0
    while q:
        c = q.popleft()
        if c == K:
            return d[c]
        for nxt in [c+1, c-1]:
            if 0<=nxt<M and d[nxt] > d[c] + 1:
                d[nxt] = d[c] + 1
                q.append(nxt)
        if 0<=c * 2< M and d[c*2] > d[c]:
            d[c*2] = d[c]
            q.append(c*2)

M = 100001
N, K = map(int, input().split())
d = [1e9] * M
print(bfs())
print(dijkstra())
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[]for _ in range(n+1)]


def is_possible(wei):
    que = deque([frm])
    v[frm] = 1
    while que:
        cur = que.popleft()
        for _, (nxt, w) in enumerate(graph[cur]):
            if w < wei or v[nxt]: continue
            if nxt == to: return True
            v[nxt] = 1
            que.append((nxt))
    return False


min_c = 1000000001
max_c = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    max_c = max(max_c, c)
    min_c = min(min_c, c)

frm, to = map(int, input().split())

ans = 0
l, r = 0, max_c
while l <= r:
    m = (l + r)//2
    v = [0] * (n + 1)
    if is_possible(m):
        ans = m
        l = m + 1
    else:
        r = m - 1
print(ans)
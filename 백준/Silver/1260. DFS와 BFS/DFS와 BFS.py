from collections import deque


def bfs(start):
    que = deque([start])
    v[start] = True
    while que:
        cur = que.popleft()
        print(cur, end=' ')
        for nxt in graph[cur]:
            if v[nxt]: continue
            que.append(nxt)
            v[nxt] = True


def dfs(cur):
    print(cur, end=' ')
    v[cur] = True
    for nxt in graph[cur]:
        if v[nxt]: continue
        dfs(nxt)


n, m, start = map(int, input().split())
graph = [[]for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, n+1):
    graph[i].sort()

v = [False] * (n+1)
dfs(start)
print()
v = [False] * (n+1)
bfs(start)
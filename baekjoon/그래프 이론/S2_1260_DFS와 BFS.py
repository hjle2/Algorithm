def dfs(i):
    visited[i] = 1
    print(i, end=' ')
    for v in edge[i]:
        if not visited[v]:
            dfs(v)

def bfs(i):
    tmp = [i]
    visited[i] = 1
    while tmp:
        i = tmp.pop(0)
        print(i, end=' ')
        for v in edge[i]:
            if not visited[v]:
                visited[v] = 1
                tmp.append(v)


N, M, V = map(int, input().split())
edge =[[]for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

for i in range(1, N+1):
    edge[i].sort()

visited = [0] * (N+1)
dfs(V)
print()
visited = [0] * (N+1)
bfs(V)
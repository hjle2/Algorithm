N = int(input())
M = int(input())
graph = [[]for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(cur):
    global ans
    for i in graph[cur]:
        if visited[i]:
            continue
        visited[i] = True
        ans += 1
        dfs(i)


ans = 0
visited = [False] * (N+1)
visited[1] = True
dfs(1)
print(ans)
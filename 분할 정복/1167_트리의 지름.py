import sys

sys.setrecursionlimit(10**6)
def dfs(now, d):
    ret = 0
    flag = False
    for i in range(0, len(line[now]), 2):
        nxt, dst = line[now][i:i+2]
        if not visited[nxt]:
            visited[nxt] = True
            ret = max(ret, dfs(nxt, d + dst))
            flag = True
            visited[nxt] = False
    return ret if flag else d


input = sys.stdin.readline
N = int(input()) + 1
line = [[]for _ in range(N)]
for i in range(1, N):
    line[i] = [*map(int, input().split())][1:-1]

visited = [False] * N
ans = 0
for i in range(1, N):
    visited[i] = True
    ans = max(ans, dfs(i, 0))
    visited[i] = False
print(ans)

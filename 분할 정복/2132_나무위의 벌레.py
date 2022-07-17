import sys

def dfs(que, v):
    now = que[-1]
    ret = v
    for i in A[now]:
        if not visited[i]:
            visited[i] = True
            ret = max(ret, dfs(que + [i], v + C[i]))
            visited[i] = False
    return ret


input = sys.stdin.readline
N = int(input())
C = [*map(int, input().split())]
A = [[]for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    A[a-1].append(b-1)
    A[b-1].append(a-1)

visited = [False] * N
s = sum(C)
ans = idx = 0
for i in range(N):
    if A[i]:
        visited[i] = True
        tmp = dfs([i], C[i])
        if tmp > ans:
            ans, idx = tmp, i
        if ans == s:
            break
        visited[i] = False
print(ans, idx+1)
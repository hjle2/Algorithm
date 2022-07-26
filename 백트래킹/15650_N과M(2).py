# def dfs(que, n):
#     if len(que) == M:
#         print(*que)
#         return
#     for i in range(n, N+1):
#         dfs(que + [i], i+1)
import itertools

N, M = map(int, input().split())
# dfs([], 1)

c = itertools.combinations(range(1, N+1), M)
for i in c:
    print(*i)
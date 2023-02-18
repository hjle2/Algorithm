# def dfs(que, n):
#     if len(que)==M:
#         print(*que)
#         return
#     for i in range(1, N+1):
#         if not v[i]:
#             v[i] = True
#             dfs(que + [i], i+1)
#             v[i] = False
#
import itertools

N, M = map(int, input().split())
# v = [False] * (N+1)
# dfs([], 1)

p = itertools.permutations(range(1, N+1), M)
for i in p:
    print(*i)
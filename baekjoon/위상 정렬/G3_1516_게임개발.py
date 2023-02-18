# 4
# 20 -1
# 10 -1
# 1 1 2 -1
# 1000 1 2 3 -1
#
# wrong
# 20
# 10
# 21
# 1020
#
# correct
# 20
# 10
# 21
# 1021

# 5
# 10 -1
# 20 1 -1
# 30 2 -1
# 40 3 5 -1
# 100 -1

# ans
# 10
# 30
# 60
# 200
# 100

import sys
from collections import deque
input = sys.stdin.readline

# N = int(input())
# time = [0] * N
# cnt = [0] * N
# visited = [False] * N
# seq = [[]for _ in range(N)]
# seq_rev = [[]for _ in range(N)]
# for i in range(N):
#     t, *a = map(int, input().split())
#     time[i] = t
#     for j in a:
#         if j == -1:
#             break
#         seq[j-1].append(i)
#         seq_rev[i].append(j-1)
#         cnt[i] += 1
#
# que = deque()
# for i in range(N):
#     if not cnt[i]:
#         que.append(i)
#         visited[i] = True
#
# while que:
#     current = que.popleft()
#     if seq_rev[current]:
#         time[current] += max(time[before]for before in seq_rev[current])
#     for nxt in seq[current]:
#         cnt[nxt] -= 1
#         if not cnt[nxt]:
#             que.append(nxt)
#
# print(*time, sep='\n')

N = int(input())
v, t, graph = [1], [0], [[]]
for i in range(N):
    l = [*map(int, input().split())]
    v.append(1)
    t.append(l[0])
    graph.append(l[1:-1])

def dfs(x):
    if not graph[x] or not v[x]:
        v[x] = 0;return
    for i in graph[x]:
        if v[i]: dfs(i)
    t[x] += max(t[i] for i in graph[x])
    v[x] = 0
for i in range(N):
    dfs(i+1)
for i in range(N):
    print(t[i+1])

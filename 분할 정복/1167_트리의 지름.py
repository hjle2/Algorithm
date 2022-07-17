# import sys
# input = sys.stdin.readline
#
# def dfs(node, sum):
#     visited[node] = True
#     global diam
#     global far_node
#     if diam < sum:
#         diam, far_node = sum, node
#
#     for i in range(0, len(line[node]), 2):
#         next_node, distance = line[node][i:i+2]
#         print(next_node, distance)
#         if not visited[next_node]:
#             dfs(next_node, sum + distance)
#
#
# N = int(input()) + 1
# line = [[]for _ in range(N)]
# for i in range(1, N):
#     line[i] = [*map(int, input().split())][1:-1]
#
# far_node = diam = 0
# visited = [False] * N
# dfs(1, 0)
# dfs(far_node, diam)
# print(diam)
from collections import defaultdict

graph = defaultdict(list)
print(graph)
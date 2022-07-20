import sys

input = sys.stdin.readline

def dfs(node, d):
    global farNode
    global distance
    visited[node] = True
    if d > distance:
        farNode, distance = node, d

    for i, j in line[node]:
        if not visited[i]:
            dfs(i, d + j)
            visited[i] = False


V = int(input()) + 1
line = [[]for _ in range(V)]
for i in range(V-1):
    tmp = [*map(int, input().split())]
    for i in range(1, len(tmp)-1, 2):
        line[tmp[0]].append([tmp[i], tmp[i+1]])

visited = [False] * V
farNode = distance = 0
dfs(1, 0)
visited[1] = False
dfs(farNode, 0)
print(distance)
# 4
# 1 2 2 4 4 -1
# 2 1 2 3 1 -1
# 3 1 2 4 3 -1
# 4 3 3 1 4 -1



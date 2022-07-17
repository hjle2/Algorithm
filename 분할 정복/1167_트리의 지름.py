import sys
from collections import defaultdict

input = sys.stdin.readline
def dfs(node, d):
    global far_node
    global diam
    visited[node] = True
    if d > diam:
        far_node, diam = node, d
    # for u, c in graph[node]:
    #     if not visited[u]:
    #         dfs(u, d + c)
    # for i in range(0, len(line[node]), 2):
    #     nxt, dst = line[node][i:i+2]
    #     if not visited[nxt]:
    #         dfs(nxt, d + dst)
    for u, c in line[node]:
        if not visited[u]:
            dfs(u, d + c)

N = int(input()) + 1
line = [[]for _ in range(N)]

for i in range(N-1):
    tmp = [*map(int, input().split())]
    key = tmp[0]
    for j in range(1, len(tmp)-1, 2):
        line[key].append(tmp[j:j+2])

# for i in range(1, N):
#     line[i] = [*map(int, input().split())][1:-1]

# graph = defaultdict(list)
# for _ in range(N-1):
#     temp = list(map(int,input().split()))
#     key = temp[0]
#     for i in range(1,len(temp)-1,2):
#         graph[key].append((temp[i],temp[i+1]))

visited = [False] * N
far_node = diam = 0
dfs(1, 0)
visited = [False] * N
dfs(far_node, 0)
print(diam)


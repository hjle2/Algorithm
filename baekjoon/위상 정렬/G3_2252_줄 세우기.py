import sys
from collections import deque

input = sys.stdin.readline



def topological_sort():
    que = deque()
    visited = [0] * N
    for i in range(N):
        if not cnt[i]:
            que.append(i)
    while que:
        x = que.popleft()
        print(x+1, end=' ')
        for nxt in edge[x]:
            cnt[nxt] -= 1
            if cnt[nxt] == 0:
                que.append(nxt)

N, M = map(int, input().split())
edge = [[]for _ in range(N)]
cnt = [0] * N
for _ in range(M):
    a, b = map(int, input().split())
    edge[a-1].append(b-1)
    cnt[b-1] += 1
topological_sort()
# N * N 크기의 공간에 물고기 M 마리와 상어 1마리가 있다
# 한 칸에는 물고기가 최대 1마리 존재한다
# 물고기와 상어는 모두 크기를 갖고 있고, 이 크기는 자연수 이다
# 처음 아기 상어의 크기는 2이고, 1초 후 상하좌우 인접한 한 칸씩 이동한다
# 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없다.
# 나머지 칸은 모두 지나갈 수 있다 (자신의 크기와 같은 물고기, 작은 물고기, 물고기가 없는 칸)
# 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다
# 어디로 이동할지 결정하는 방법은 아래와 같다
# 먹을 수 있는 물고기가 1마리라면 그 물고기를 먹으러 간다
# 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다
# 거리는 아기상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때 지나야 하는 칸의 개수의 최솟값이다
# 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면 가장 왼쪽의 물고기를 먹는다.
# 상어의 크기는 자신의 크기와 같은 수의 물고기를 먹을 때마다 크기가 1 증가한다
# 상어가 엄마 상어에게 도움을 요청하지 않고 물고기를 얼마나 잡아먹는지 구하라

import sys
from collections import deque
input = sys.stdin.readline

def nextPt(x, y, now_s):
    que = deque([(x, y, 0)])
    v = [[False]*N for _ in range(N)]
    v[x][y] = True
    ax, ay  = [N, N]
    while que:
        size = len(que)
        while size:
            size -= 1
            x, y, d = que.popleft()
            for dx, dy in D:
                nx, ny = x + dx, y + dy
                if 0<=nx<N and 0<=ny<N and not v[nx][ny] and A[nx][ny] <= now_s:
                    if 0 < A[nx][ny] < now_s:
                        if nx < ax:
                            ax, ay = nx, ny
                        elif nx == ax and ny < ay:
                            ax, ay = nx, ny
                    que.append((nx, ny, d + 1))
                    v[nx][ny] = True
        if ay < N:
            return [ax, ay, d+1]
    return []

N = int(input())
D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
A = [[]for _ in range(N)]
x = y = 0
for i in range(N):
    ar = [*map(int, input().split())]
    A[i] = ar
    for j in range(N):
        if ar[j] == 9:
            x, y = i, j
            A[i][j] = 0
t = 0
s = 2
fcnt = 0
while 1:
    pt = nextPt(x, y, s)
    if not pt:
        break
    t += pt.pop()
    x, y = pt
    A[x][y] = 0
    fcnt += 1
    if fcnt == s:
        fcnt, s = 0, s+1
print(t)
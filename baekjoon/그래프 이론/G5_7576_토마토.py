from copy import deepcopy


def spread(x, y):
    global total
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0<=nx<N and 0<=ny<M and T[nx][ny] == 0:
            tmp.append((nx, ny))
            T[nx][ny] = 1
            total -= 1

M, N = map(int, input().split())
T = [[*map(int, input().split())]for _ in range(N)]
tom = []
total = 0
for i in range(N):
    for j in range(M):
        if T[i][j] == 1:
            tom.append((i, j))
        elif T[i][j] == 0:
            total+=1

tmp = []
day = 0
while tom:
    for x, y in tom:
        spread(x, y)
    tom = deepcopy(tmp)
    tmp.clear()
    day += 1
if total: print(-1)
else: print(day-1)

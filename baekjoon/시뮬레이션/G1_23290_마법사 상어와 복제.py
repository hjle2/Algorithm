from copy import deepcopy

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

dx_s = [-1, 0, 1, 0]
dy_s = [0, -1, 0, 1]

fish_n, S = map(int, input().split())
tank = [[[]for _ in range(4)]for _ in range(4)]

for _ in range(fish_n):
    x, y, d = map(int, input().split())
    tank[x-1][y-1].append(d-1)

sx, sy = map(int, input().split())
shark = (sx-1, sy-1)

smell = [[0] * 4 for _ in range(4)]


def move_fish():
    ret = [[[]for _ in range(4)]for _ in range(4)]
    for x in range(4):
        for y in range(4):
            while temp[x][y]:
                d = temp[x][y].pop()
                nx, ny, nd = move(x, y, d)
                ret[nx][ny].append(nd)
    return ret


def move(x, y, d):
    for i in range(d, d-8, -1):
        i %= 8
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < 4 and 0 <= ny < 4 and shark != (nx, ny) and not smell[nx][ny]:
            return nx, ny, i
    return x, y, d


def move_shark(x, y, dep, dir, cnt, visit):
    global max_eat, smaller_dir, shark, shark_path
    if dep == 0:
        if max_eat < cnt or (max_eat == cnt and dir < smaller_dir):
            max_eat = cnt
            smaller_dir = dir
            shark = (x, y)
            shark_path = visit
        return

    for d in range(4):
        nx, ny = x + dx_s[d], y + dy_s[d]
        if 0 <= nx < 4 and 0 <= ny < 4:
            if (nx, ny) in visit:
                move_shark(nx, ny, dep-1, dir * 10 + d, cnt, visit)
            else:
                move_shark(nx, ny, dep-1, dir * 10 + d, cnt + len(temp[nx][ny]), visit + [(nx, ny)])


def remove_smell():
    for r in range(4):
        for c in range(4):
            if smell[r][c]:
                smell[r][c] -= 1


for _ in range(S):
    temp = deepcopy(tank)

    temp = move_fish()

    max_eat, smaller_dir, shark_path = -1, 0, []
    move_shark(shark[0], shark[1], 3, 0, 0, [])

    for x, y in shark_path:
        if temp[x][y]:
            temp[x][y] = []
            smell[x][y] = 3

    remove_smell()

    for r in range(4):
        for c in range(4):
            tank[r][c] += temp[r][c]

cnt = 0
for r in range(4):
    for c in range(4):
        cnt += len(tank[r][c])
print(cnt)

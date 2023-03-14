import sys
from collections import deque

def read_input():
    rx = ry = bx = by = 0
    for i in range(n):
        ar[i] = [*input().rstrip()]
        for j in range(m):
            if ar[i][j] == 'R':
                rx, ry = i, j
            elif ar[i][j] == 'B':
                bx, by = i, j
    return rx, ry, bx, by

def get_move_pt(x, y, ox, oy, d):
    flag = False
    while ar[x][y] != '#' and ar[x][y] != 'O':
        x += dx[d]; y += dy[d]
        if x == ox and y == oy:
            flag = True
    if ar[x][y] == '#':
        x -= dx[d]; y -= dy[d]
        if flag: x -= dx[d]; y -= dy[d]
    return x, y

def move(rx, ry, bx, by, d):
    # blue ball
    x, y = get_move_pt(bx, by, rx, ry, d)
    if ar[x][y] == 'O':
        return False

    # red ball
    r, c = get_move_pt(rx, ry, bx, by, d)
    return r, c, x, y


def get_ans(rx, ry, bx, by): # bfs방식 선택 dfs방식으로도 해결 가능하나 백트래킹 조건 필요
    v[rx][ry][bx][by] = True
    q = deque([(rx, ry, bx, by, 1)])
    while q:
        rx, ry, bx, by, c = q.popleft()
        if c > 10: return -1
        for d in range(4):
            move_ret = move(rx, ry, bx, by, d)
            # blue ball -> O
            if not move_ret: continue
            rr, rc, br, bc = move_ret
            # red ball -> O
            if ar[rr][rc] == 'O': return c
            if v[rr][rc][br][bc]: continue
            v[rr][rc][br][bc] = True
            q.append((rr, rc, br, bc, c+1))
    return -1


input = sys.stdin.readline
n, m = map(int, input().split())
ar = [[]for _ in range(n)]
v = [[[[False] * m for _ in range(n)]for _ in range(m)]for _ in range(n)]
rx, ry, bx, by = read_input()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
print(get_ans(rx, ry, bx, by))

from collections import deque
from copy import deepcopy

n, m = map(int, input().split())
board = [[*input().strip()]for _ in range(n)]

def get_pt(board):
    for r in range(n):
        for c in range(m):
            if board[r][c] == 'R':
                board[r][c] = '.'
                rr, rc = r, c
            if board[r][c] == 'B':
                br, bc = r, c
                board[r][c] = '.'
    return rr, rc, br, bc

dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def roll_pt(r, c, x, y, d):
    flag = False # 굴리는 중에 x, y를 만났는지!
    while board[r][c] == '.':
        r += dir[d][0]
        c += dir[d][1]

        if (r, c) == (x, y):
            flag = True

    if board[r][c] == 'O':
        return r, c
    if flag:
        r -= dir[d][0]
        c -= dir[d][1]
    r -= dir[d][0]
    c -= dir[d][1]

    return r, c


def roll(rr, rc, br, bc, d):
    nrr, nrc = roll_pt(rr, rc, br, bc, d)
    nbr, nbc = roll_pt(br, bc, rr, rc, d)
    return nrr, nrc, nbr, nbc


rr, rc, br, bc = get_pt(board)
v = [[[[False] * m for _ in range(n)]for _ in range(m)]for _ in range(n)]
v[rr][rc][br][bc] = True
que = deque([(rr, rc, br, bc, 0)])

while que:
    rr, rc, br, bc, cnt = que.popleft()
    if cnt >= 10: continue
    for d in range(4):
        trr, trc, tbr, tbc = roll(rr, rc, br, bc, d)
        if board[tbr][tbc] == 'O':# blue가 빠졌으면
            continue
        if board[trr][trc] == 'O':# red가 빠진 경우
            print(cnt+1)
            exit(0)

        if not v[trr][trc][tbr][tbc]:
            que.append((trr, trc, tbr, tbc, cnt+1))
print(-1)


from collections import deque

n, m, k = map(int, input().split())
board = [[*map(int, input().split())]for _ in range(n)]

di = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def in_range(r, c):
    return 0 <= r < n  and 0 <= c < n



# 새로운 헤드 구하기
def get_new_head(r, c):
    rr, rc = 0, 0
    for dr, dc in di:
        nr, nc = r + dr, c + dc
        if not in_range(nr, nc): continue

        if board[nr][nc] == 4:
            return nr, nc
        if board[nr][nc] == 3: # 머리와 꼬리가 닿아있는 경우
            rr, rc = nr, nc

    return rr, rc


# 새로운 꼬리 구하기
def get_new_tail(r, c):
    for dr, dc in di:
        nr, nc = r + dr, c + dc
        if not in_range(nr, nc): continue
        # 2인 칸 찾기
        if board[nr][nc] == 2:
            return nr, nc


# 헤드 또는 꼬리 찾기
def get_head_tail(r, c, h):
    v = [[False] * n for _ in range(n)]
    que = deque([(r, c)])
    v[r][c] = True
    while que:
        r, c = que.popleft()
        if board[r][c] == h:
            return r, c

        for dr, dc in di:
            nr, nc = r + dr, c + dc
            if not in_range(nr, nc) or v[nr][nc]: continue
            if board[nr][nc]:
                que.append((nr, nc))
            v[nr][nc] = True


# 헤드가 r, c인 팀 한칸씩 이동
def move_team(r, c):
    hr, hc = get_new_head(r, c) # 새로운 머리 좌표
    otr, otc = get_head_tail(r, c, 3) # 꼬리 좌표
    tr, tc = get_new_tail(otr, otc) # 새로운 꼬리 좌표

    board[otr][otc] = 4 # 기존의 꼬리는 아무것도 아닌걸로!
    board[hr][hc] = 1 # 새로운 헤드
    board[r][c] = 2 # 원래의 헤드는 중간으로
    board[tr][tc] = 3 # 새로운 꼬리

    visited[hr][hc] = True # 이미 이동처리한 팀의 새로운 헤드에 대해서 이동처리하지 않도록!


def move():
    for r in range(n):
        for c in range(n):
            if not visited[r][c] and board[r][c] == 1: # 헤드를 만날 경우
                # 앞으로 한칸 이동
                visited[r][c] = True
                move_team(r, c)


def get_th(r, c):
    x, y = r, c
    hr, hc = get_head_tail(r, c, 1)

    v = [[False] * n for _ in range(n)]
    v[hr][hc] = True

    if x == hr and y == hc: return 1
    for dr, dc in di:
        nr, nc = hr + dr, hc + dc
        if in_range(nr, nc) and board[nr][nc] == 2:
            r, c = nr, nc
            break
    if x == r and y == c: return 2
    que = deque([(r, c)])
    v[r][c] = True
    cnt = 1
    while que:
        r, c = que.popleft()
        cnt += 1
        if r == x and c == y:
            return cnt

        for dr, dc in di:
            nr, nc = r + dr, c + dc
            if not in_range(nr, nc) or v[nr][nc]: continue
            if board[nr][nc]:
                que.append((nr, nc))
            v[nr][nc] = True


def throw(round):
    if round // n % 4 in [0, 2]: # 좌, 우
        if round // n % 4 == 0:
            r = round % n
            for c in range(n):
                if 0 < board[r][c] < 4:
                    th = get_th(r, c)
                    change_dir(r, c)
                    return th * th
        else:
            r = n - 1 - round % n
            for c in range(n-1, -1, -1):
                if 0 < board[r][c] < 4:
                    th = get_th(r, c)
                    change_dir(r, c)
                    return th * th

    else:
        if round // n % 4 == 1:
            c = round % n
            for r in range(n-1, -1, -1):
                if 0 < board[r][c] < 4:
                    th = get_th(r, c)
                    change_dir(r, c)
                    return th * th
        else:
            c = n - 1 - round % n
            for r in range(n):
                if 0 < board[r][c] < 4:
                    th = get_th(r, c)
                    change_dir(r, c)
                    return th * th
    return 0


def change_dir(r, c):
# head -> tail
# tail -> head
    hr, hc = get_head_tail(r, c, 1)
    tr, tc = get_head_tail(r, c, 3)
    board[hr][hc] = 3
    board[tr][tc] = 1

score = 0
for i in range(k):
    visited = [[False] * n for _ in range(n)]
    move()
    tmp = throw(i)
    score += tmp
    # change_dir()
print(score)

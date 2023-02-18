from collections import deque


def destroy(h, flag):
    c = -1
    if flag:
        for c in range(C):
            if A[h][c] == 'x':
                A[h][c] = '.'
                break
    else:
        for c in range(C-1, -1, -1):
            if A[h][c] == 'x':
                A[h][c] = '.'
                break

    for dr, dc in d:
        nr, nc = h + dr, c + dc
        if 0<=nr<R and 0<=nc<C and A[nr][nc] == 'x':
            DQ.append((nr, nc))


def fall(vis, fall_list):
    k, flag = 1, 0
    while True:
        for r, c in fall_list:
            if r + k == R-1:
                flag = 1
                break
            if A[r+k+1][c] == 'x' and not vis[r+k+1][c]:
                flag = 1
                break
        if flag:
            break
        k += 1

    for r in range(R-2, -1, -1):
        for c in range(C):
            if A[r][c] == 'x' and vis[r][c]:
                A[r][c] = '.'
                A[r+k][c] = 'x'


def dfs(r, c):
    que = deque([(r, c)])
    vis = [[False]*C for _ in range(R)]
    vis[r][c] = True
    cluster = []

    while que:
        r, c = que.popleft()
        if r == R-1: return
        if A[r+1][c] == '.':
            cluster.append((r, c))

        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if 0<=nr<R and 0<=nc<C and not vis[nr][nc] and A[nr][nc] == 'x':
                que.append((nr, nc))
                vis[nr][nc] = True

    fall(vis, cluster)


R, C = map(int, input().split())
A = [[*input()] for _ in range(R)]
N = int(input())
H = map(int, input().split())
DQ = deque([])
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

left = True
for h in H:
    h = R-h
    destroy(h, left)
    left = not left
    while DQ:
        r, c = DQ.popleft()
        dfs(r, c)

for r in A:
    print(*r, sep='')

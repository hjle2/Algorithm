n, m = map(int, input().split())
board = [[*input()] for _ in range(n)]

r, c = 0, 0
que = [(r, c, 1)]
v = [[False] * m for _ in range(n)]
v[r][c] = True

while que:
    r, c, d = que.pop(0)
    if r == n-1 and c == m-1:
        print(d)
        break

    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == '1' and not v[nr][nc]:
            que.append((nr, nc, d+1))
            v[nr][nc] = True


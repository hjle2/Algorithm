def draw(r, c):
    ar[r][c:c+3] = '***'
    ar[r+1][c:c+3] = '* *'
    ar[r+2][c:c+3] = '***'


def dfs(n, r, c):
    if n == 3:
        draw(r, c)
        return
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            nr, nc = r + i * n//3, c + j * n//3
            dfs(n//3, nr, nc)


N = int(input())
ar = [[' ']*N for _ in range(N)]
dfs(N, 0, 0)
for i in range(N):
    print(*ar[i], sep='')

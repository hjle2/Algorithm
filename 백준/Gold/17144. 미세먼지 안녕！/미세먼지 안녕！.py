def spread():
    new_board = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if board[i][j] > 0:
                tmp = board[i][j] // 5
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < r and 0 <= nj < c and board[ni][nj] != -1:
                        new_board[ni][nj] += tmp
                        new_board[i][j] -= tmp

    for i in range(r):
        for j in range(c):
            board[i][j] += new_board[i][j]


def work():
    # 반시계 방향 순환
    x = conditioner[0]

    # 아래로
    for i in range(x-1, 0, -1):
        board[i][0] = board[i-1][0]

    # 왼쪽으로
    for i in range(0, c-1):
        board[0][i] = board[0][i+1]

    # 위로
    for i in range(0, x):
        board[i][c-1] = board[i+1][c-1]

    # 오른쪽으로
    for i in range(c-1, 0, -1):
        board[x][i] = board[x][i-1]

    board[x][1] = 0
    # 시계방향 순환
    x = conditioner[1]
    for i in range(x+1, r-1):
        board[i][0] = board[i+1][0]

    for i in range(0, c-1):
        board[r-1][i] = board[r-1][i+1]

    # 아래로
    for i in range(r-1, x, -1):
        board[i][c-1] = board[i-1][c-1]

    # 오른쪽으로
    for i in range(c-1, 0, -1):
        board[x][i] = board[x][i-1]

    board[x][1] = 0


r, c, t = map(int, input().split())
board = [[*map(int, input().split())]for _ in range(r)]
conditioner = []

for i in range(r):
    if board[i][0] == -1:
        conditioner.append(i)

for _ in range(t):
    spread()
    work()

ans = 0
for i in range(r):
    for j in range(c):
        if board[i][j] > 0:
            ans += board[i][j]
print(ans)
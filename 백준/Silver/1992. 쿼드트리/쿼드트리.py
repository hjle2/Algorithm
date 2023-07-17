def solve(size, i, j):
    print('(', end='')

    nxt_size = size // 2
    if isallsame(nxt_size, i, j):
        print(board[i][j], end='')
    else:
        solve(nxt_size, i, j)

    if isallsame(nxt_size, i, j + nxt_size):
        print(board[i][j + nxt_size], end='')
    else:
        solve(nxt_size, i, j + nxt_size)

    if isallsame(nxt_size, i + nxt_size, j):
        print(board[i + nxt_size][j], end='')
    else:
        solve(nxt_size, i + nxt_size, j)

    if isallsame(nxt_size, i + nxt_size, j + nxt_size):
        print(board[i + nxt_size][j + nxt_size], end='')
    else:
        solve(nxt_size, i + nxt_size, j + nxt_size)

    print(')', end='')


def isallsame(size, i, j):
    for x in range(size):
        for y in range(size):
            if board[x+i][y+j] != board[i][j]:
                return False
    return True


n = int(input())
board = [[*map(int, [*input()])]for _ in range(n)]
if isallsame(n, 0, 0):
    print(board[0][0], end='')
else:
    solve(n, 0, 0)
from copy import deepcopy

r, c = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(r)]


# 3개의 벽을 세울 수 있다
# 꼭 3개를 세워야 함
# 0은 빈칸, 1은 벽, 2는 바이러스
def dfs(depth):
    if depth == 3:
        global ans
        ans = max(ans, get_count(deepcopy(board)))
        return

    for i in range(r):
        for j in range(c):
            if board[i][j] == 0:
                board[i][j] = 1
                dfs(depth + 1)
                board[i][j] = 0


def get_count(board):
    board = spread(board)
    return count(board, 0)


def spread(board):
    virus = get_virus(board)
    while virus:
        for x, y in virus:
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if in_range(nx, ny) and board[nx][ny] == 0:
                    board[nx][ny] = 2
        new_virus = get_virus(board)
        if len(virus) != len(new_virus):
            virus = new_virus
        else:
            break
    return board


def in_range(x, y):
    return 0 <= x < r and 0 <= y < c


def get_virus(board):
    ret = []
    for i in range(r):
        for j in range(c):
            if board[i][j] == 2:
                ret.append((i, j))
    return ret


def count(board, target):
    ret = 0
    for i in range(r):
        for j in range(c):
            if board[i][j] == target:
                ret += 1
    return ret

ans = 0
dfs(0)
print(ans)
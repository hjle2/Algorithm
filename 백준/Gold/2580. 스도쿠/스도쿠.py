def get_ans(x, y):
    v = [False] * (n+1)
    for i in range(n):
        v[board[x][i]] = True
        v[board[i][y]] = True

    sx, sy = x // 3 * 3, y // 3 * 3

    for i in range(3):
        for j in range(3):
            v[board[sx+i][sy+j]] = True

    ans = []
    for i in range(1, n+1):
        if not v[i]:
            ans.append(i)
    return ans


def dfs(idx):
    global ans
    if ans: return
    if len(zero) == idx:
        ans = True
        for i in range(n):
            print(*board[i])
        return

    x, y = zero[idx]
    pts = get_ans(x, y)
    for num in pts:
        board[x][y] = num
        dfs(idx + 1)
        board[x][y] = 0


n = 9
board = [[*map(int, input().split())]for _ in range(n)]

zero = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 0:
            zero.append((i, j))

ans = False
dfs(0)

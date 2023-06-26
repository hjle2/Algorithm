from copy import deepcopy


def get_max(board):
    ret = 0
    for i in range(n):
        ret = max(ret, max(board[i]))
    return ret


def dfs(direction, board, depth):
    if depth == 5:
        global ans
        for i in range(n):
            ans = max(ans, max(board[i]))
        return

    ar = [[0] * n for _ in range(n)]

    if direction == 0:
        for i in range(n):
            tmp = []
            flag = False
            for j in range(n):
                if board[i][j]:
                    if tmp and not flag and tmp[-1] == board[i][j]:
                        tmp.append(board[i][j] + tmp.pop())
                        flag = True
                    else:
                        tmp.append(board[i][j])
                        flag = False
            for j in range(n - len(tmp)):
                tmp.append(0)
            ar[i] = tmp
    elif direction == 2:
        for i in range(n):
            tmp = []
            flag = False
            for j in range(n-1, -1, -1):
                if board[i][j]:
                    if tmp and not flag and tmp[-1] == board[i][j]:
                        tmp.append(board[i][j] + tmp.pop())
                        flag = True
                    else:
                        tmp.append(board[i][j])
                        flag = False
            for j in range(n - len(tmp)):
                tmp.append( 0)
            ar[i] = tmp[::-1]

    elif direction == 1:
        for i in range(n):
            tmp = []
            flag = False
            for j in range(n):
                if board[j][i]:
                    if tmp and not flag and tmp[-1] == board[j][i]:
                        tmp.append(board[j][i] + tmp.pop())
                        flag = True
                    else:
                        tmp.append(board[j][i])
                        flag = False
            for j in range(n - len(tmp)):
                tmp.append(0)
            for j in range(n):
                ar[j][i] = tmp[j]

    elif direction == 3:
        for i in range(n):
            tmp = []
            flag = False
            for j in range(n-1, -1, -1):
                if board[j][i]:
                    if tmp and not flag and tmp[-1] == board[j][i]:
                        tmp.append(board[j][i] + tmp.pop())
                        flag = True
                    else:
                        tmp.append(board[j][i])
                        flag = False
            for j in range(n - len(tmp)):
                tmp.append(0)
            for j in range(n):
                ar[j][i] = tmp[n-j-1]

    for d in range(4):
        dfs(d, deepcopy(ar), depth + 1)


n = int(input())
ar = [[*map(int, input().split())]for _ in range(n)]
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
ans = 0
for i in range(4):
    dfs(i, deepcopy(ar), 0)
print(ans)
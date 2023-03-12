from copy import deepcopy

n = int(input())
board = [[*map(int, input().split())]for _ in range(n)]


def get_max(board):
    ans = 0
    for i in range(n):
        ans = max(ans, max(board[i]))
    return ans


def push(d, board): # d 방향으로 board를 민다
    new_board = [[0]* n for _ in range(n)]
    if d == 0: # 왼쪽으로 미는 경우
        for r in range(n):
            idx = 0
            push_flag = False
            for c in range(n):
                if not board[r][c]: continue
                if idx > 0 and new_board[r][idx-1] == board[r][c] and not push_flag:
                    new_board[r][idx-1] += board[r][c]
                    push_flag = True
                    idx -= 1
                else:
                    new_board[r][idx] = board[r][c]
                    push_flag = False
                idx += 1

    elif d == 1: # 오른쪽으로 미는 경우
        for r in range(n):
            idx = n-1
            push_flag = False
            for c in range(n-1, -1, -1):
                if not board[r][c]: continue
                if idx + 1 < n and new_board[r][idx+1] == board[r][c] and not push_flag:
                    new_board[r][idx+1] += board[r][c]
                    push_flag = True
                    idx += 1
                else:
                    new_board[r][idx] = board[r][c]
                    push_flag = False
                idx -= 1
    elif d == 2: # 위로 미는 경우
        for c in range(n):
            idx = 0
            push_flag = False
            for r in range(n):
                if not board[r][c]: continue
                if idx > 0 and new_board[idx-1][c] == board[r][c] and not push_flag:
                    new_board[idx-1][c] += board[r][c]
                    push_flag = True
                    idx -= 1
                else:
                    new_board[idx][c] = board[r][c]
                    push_flag = False
                idx += 1
    else: # 위로 미는 경우
        for c in range(n):
            idx = n-1
            push_flag = False
            for r in range(n-1, -1, -1):
                if not board[r][c]: continue
                if idx+1 < n and new_board[idx+1][c] == board[r][c] and not push_flag:
                    new_board[idx+1][c] += board[r][c]
                    push_flag = True
                    idx += 1
                else:
                    new_board[idx][c] = board[r][c]
                    push_flag = False
                idx -= 1
    return new_board


def dfs(cnt, board):
    global ans
    if cnt == 5:
        ans = max(ans, get_max(board))
        return
    for d in range(4):
        new_board = push(d, board)
        dfs(cnt+1, new_board)


ans = 0
dfs(0, board)
print(ans)


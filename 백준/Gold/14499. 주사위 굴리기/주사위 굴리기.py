n, m, x, y, k = map(int, input().split())
board = [[*map(int, input().split())]for _ in range(n)]

# 0: 윗면, 1: 아래면, 2: 왼쪽면, 3: 오른면, 4: 앞면, 5: 뒷면
square = [0] * 6

def turn(d, square):
    new_squre = [0] * 6
    if d == 1: # 동쪽
        new_squre[0] = square[2]
        new_squre[1] = square[3]
        new_squre[2] = square[1]
        new_squre[3] = square[0]
        new_squre[4] = square[4]
        new_squre[5] = square[5]
    elif d == 2: # 서쪾
        new_squre[0] = square[3]
        new_squre[1] = square[2]
        new_squre[2] = square[0]
        new_squre[3] = square[1]
        new_squre[4] = square[4]
        new_squre[5] = square[5]
    elif d == 3: # 북쪾
        new_squre[0] = square[4]
        new_squre[1] = square[5]
        new_squre[4] = square[1]
        new_squre[5] = square[0]
        new_squre[2] = square[2]
        new_squre[3] = square[3]
    elif d == 4: # 남쪽
        new_squre[0] = square[5]
        new_squre[1] = square[4]
        new_squre[4] = square[0]
        new_squre[5] = square[1]
        new_squre[2] = square[2]
        new_squre[3] = square[3]
    return new_squre


dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
for d in map(int, input().split()):
    x += dx[d]
    y += dy[d]
    if x < 0:
        x = 0
        continue
    if y < 0:
        y = 0
        continue
    if x >= n:
        x = n-1
        continue
    if y >= m:
        y = m-1
        continue
    square = turn(d, square)
    if board[x][y]:
        square[1] = board[x][y]
        board[x][y] = 0
    else:
        board[x][y] = square[1]
    print(square[0])
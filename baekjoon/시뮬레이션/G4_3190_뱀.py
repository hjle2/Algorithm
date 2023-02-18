# 뱀이 나와서 기어다니는 게임
# 사과를 먹으면 뱀의 길이가 늘어난다
# 뱀이 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다

# 뱀은 매 초마다 이동하고, 규칙은 다음과 같다
# 몸 길이를 늘려 머리를 다음칸에 위치시킨다
# 이동한 칸에 사과가 있다면 사과는 없어지고, 꼬리는 움직이지 않는다
# 사과가 없다면, 길이를 줄여 꼬리가 위치한 칸을 비워준다

# 게임이 몇 초에 끝나는지 구하라

N = int(input())
board = [[0]*N for _ in range(N)]
K = int(input())
for _ in range(K):
    x, y = map(int, input().split())
    board[x-1][y-1] = 2
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
L = int(input())
turn = [input().split()for _ in range(L)]
x, y, d = 0, 0, 0
body = [(x, y)]
board[x][y] = 1
t = 0
tt = int(turn[0][0])
while 1:
    t += 1
    x, y = x + dx[d], y + dy[d]
    if x < 0 or y < 0 or x >= N or y >= N or board[x][y] == 1:
        break
    if board[x][y] == 0:
        board[body[0][0]][body.pop(0)[1]] = 0
    body.append((x, y))
    board[x][y] = 1
    if tt == t:
        tc = turn.pop(0)[1]
        if tc == 'L':
            d = (d-1) % 4
        else:
            d = (d+1) % 4
        if turn:
            tt = int(turn[0][0])
print(t)
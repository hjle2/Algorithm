def move(d):
    x, y = snake[0]
    nx, ny = x + direction[d][0], y + direction[d][1]
    if not (1 <= nx <= n and 1 <= ny <= n) or (nx, ny) in snake:
        return True
    snake.insert(0, (nx, ny))
    if (nx, ny) not in apples:  # 사과를 먹지 않았다면 꼬리가 따라옴
        snake.pop()
    else:
        apples.remove((nx, ny))


n = int(input())
k = int(input())
apples = []
for i in range(k):
    r, c = map(int, input().split())
    apples.append((r, c))
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

snake = [(1, 1)]
l = int(input())
cur_d = 0
ans = 0
prv_t = 0
for i in range(l):
    t, d = input().split()
    t = int(t)
    ret = False
    for j in range(t-prv_t):
        ret = move(cur_d)
        ans += 1
        if ret:
            break
    prv_t = t
    if ret:
        break
    if d == 'L':
        cur_d = (cur_d - 1) % 4
    else:
        cur_d = (cur_d + 1) % 4
while not ret:
    ans += 1
    if move(cur_d): break
print(ans)
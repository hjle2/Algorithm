n = int(input())
ans = [[' '] * n for _ in range(n)]


def draw(x, y):
    for i in range(3):
        ans[x][y+i] = '*'
    ans[x+1][y] = '*'
    ans[x+1][y+2] = '*'
    for i in range(3):
        ans[x+2][y+i] = '*'


def divide(n, x, y):
    n = n//3
    if n == 1:
        draw(x, y)
        return

    for i in range(3):
        divide(n, x, y + i * n)
    divide(n, x + n, y)
    divide(n, x + n, y + 2 * n)
    for i in range(3):
        divide(n, x + 2 * n, y + i * n)


divide(n, 0, 0)
for i in range(n):
    print(''.join(ans[i]))


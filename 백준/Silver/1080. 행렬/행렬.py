def flip(x, y):
    for i in range(3):
        for j in range(3):
            a[x + i][y + j] = 0 if a[x + i][y + j] else 1


def equal():
    for i in range(n):
        for j in range(m):
            if a[i][j] != b[i][j]:
                return False
    return True


n, m = map(int, input().split())
a = [[*map(int, [*input().rstrip()])]for _ in range(n)]
b = [[*map(int, [*input().rstrip()])]for _ in range(n)]

ans = 0
for i in range(n-2):
    for j in range(m-2):
        if a[i][j] != b[i][j]:
            flip(i, j)
            ans += 1
print(ans if equal() else -1)
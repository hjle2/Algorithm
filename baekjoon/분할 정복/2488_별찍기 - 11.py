# N 은 항상 3 * 2^k
import math

def draw(r, c):
    ar[r][c] = '*'
    ar[r+1][c-1] = ar[r+1][c+1] = '*'
    ar[r+2][c-2:c+3] = '*' * 5


def triangle(h, r, c):
    if h == 3:
        draw(r, c)
        return
    triangle(h//2, r, c)
    triangle(h//2, r + h//2, c - h//2)
    triangle(h//2, r + h//2, c + h//2)

N = int(input())
K = int(math.log2(N//3))
n = 5 * 2 ** K + 2 ** K - 1
ar = [[' '] * n for _ in range(N)]
triangle(N, 0, N-1)
for i in range(N):
    print(*ar[i], sep='')

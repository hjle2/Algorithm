def solve(n, r, c):
    if r < 2 and c < 2:
        return r * 2 + c
    ret = 0
    n = n >> 1
    if c >= n:
        ret += n * n
        c -= n
    if r >= n:
        ret += n * n << 1
        r -= n
    return ret + solve(n, r, c)

N, R, C = map(int, input().split())
print(solve(1<<N, R, C))
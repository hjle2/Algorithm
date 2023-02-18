def multiply(a1, a2):
    ret = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            e = 0
            for k in range(N):
                e += a1[i][k] * a2[k][j]
            ret[i][j] = e % p
    return ret

def power(ar, a):
    if a == 1:
        return ar
    ret = power(ar, a//2)
    ret = multiply(ret, ret)

    if a%2:
        ret = multiply(ret, ar)
    return ret

N, B = map(int, input().split())
A = [[*map(int, input().split())]for _ in range(N)]
p = 1000
for r in range(N):
    for c in range(N):
        A[r][c] %= p
ans = power(A, B)
for r in ans: print(*r)
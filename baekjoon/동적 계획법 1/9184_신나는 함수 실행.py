def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        a = b = c = 20
    if W[a-1][b-1][c-1]:
        return W[a-1][b-1][c-1]
    if a < b < c:
        W[a-1][b-1][c-1] = w(a, b, c-1) + w(a, b-1, c-2) - w(a, b-1, c)
    else:
        W[a-1][b-1][c-1] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return W[a-1][b-1][c-1]


N = 20
W = [[[0]*N for _ in range(N)]for _ in range(N)]

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    s = 'w(' + ', '.join([str(a), str(b), str(c)]) + ') ='
    print(s, w(a, b, c))
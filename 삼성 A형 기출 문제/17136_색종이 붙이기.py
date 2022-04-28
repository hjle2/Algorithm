def issize(r, c, s):
    if c+s > N or r+s > N: return False
    for i in range(r, r+s):
        if A[i][c+s-1]==0: return False
    for i in range(c, c+s):
        if A[r+s-1][i]==0: return False
    return True


def getsize(r, c):
    for i in range(1, 6):
        if not issize(r, c, i):
            return i-1
    return 5


def cover(r, c, s, flag):
    for i in range(r, r+s):
        for j in range(c, c+s):
            A[i][j] = flag


def sol(n):
    global ans
    while n < 100 and not A[n//N][n%N]:
        n += 1
    if n == 100:
        ans = min(ans, sum(paper))
        return
    r, c = n//N, n%N
    s = getsize(r, c)
    for i_s in range(1, s+1):
        if paper[i_s-1] < 5:
            paper[i_s-1] += 1
            cover(r, c, i_s, 0)
            sol(n+1)
            cover(r, c, i_s, 1)
            paper[i_s-1] -= 1


N = 10
A = [list(map(int, input().split()))for _ in range(N)]
paper = [0]*5
ans = 26
sol(0)
print(ans if ans < 26 else -1)

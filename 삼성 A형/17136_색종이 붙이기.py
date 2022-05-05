def isok(r, c, s):
    if r+s>n or c+s>n: return
    for i in range(s):
        if a[r+i][c+s-1]==0 or a[r+s-1][c+i]==0:
            return
    return True

def getsize(r, c):
    for s in range(2, 6):
        if not isok(r, c, s):
            return s-1
    return 5

def cover(r, c, s, f):
    for i in range(s):
        for j in range(s):
            a[r+i][j+c] = f

def dfs(i):
    global ans
    if ans<sum(paper): return
    while i<n*n and a[i//n][i%n]==0:
        i += 1
    if i==n*n:
        ans = min(ans, sum(paper))
        return
    r, c = i//n, i%n
    s = getsize(r, c)
    for i_s in range(1, s+1):
        if paper[i_s-1]<5:
            paper[i_s-1] += 1
            cover(r, c, i_s, 0)
            dfs(i+1)
            cover(r, c, i_s, 1)
            paper[i_s-1] -= 1


n = 10
a = [list(map(int, input().split()))for _ in range(10)]
paper = [0]*5
ans = 26
dfs(0)
print(ans if ans<26 else -1)

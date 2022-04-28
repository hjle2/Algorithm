dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c, d):
    ret = d
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < n and 0 <= nc < n:
            if ar[nr][nc] < ar[r][c]:
                ret = max(ret, dfs(nr, nc, d+1))
    return ret



def gettoplist():
    top = max(map(max, ar))
    ret = []
    for r in range(n):
        for c in range(n):
            if ar[r][c] == top:
                ret.append((r,c))
    return ret


def sol():
    ans = 1
    for r in range(n):
        for c in range(n):
            for ik in range(1, k+1):
                ar[r][c] -= ik
                for i,j in lst_top:
                    if i==r and j==c: continue
                    ans = max(ans, dfs(i, j, 1))
                ar[r][c] += ik
    return ans


for t in range(int(input())):
    n, k = map(int,input().split())
    ar = [list(map(int, input().split()))for _ in range(n)]
    lst_top = gettoplist()
    print(f'#{t+1}', sol())

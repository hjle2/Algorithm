dr=[1, -1, 0, 0]
dc=[0, 0, 1, -1]

def func(ar, c):
    r = 0
    cnt = 0
    while r < h and ar[r][c]==0:
        r += 1
    if r == h:
        return ar
    que = [(r,c,ar[r][c])]
    ar[r][c] = 0
    while que:
        r, c, v = que.pop(0)
        cnt += 1
        if v == 1: continue
        for i in range(4):
            nr, nc = r, c
            for _ in range(v-1):
                nr, nc = nr + dr[i], nc + dc[i]
                if 0<=nr<h and 0<=nc<w:
                    if ar[nr][nc]:
                        que.append((nr, nc, ar[nr][nc]))
                        ar[nr][nc] = 0
                else: break

    tmp = [[0]*w for _ in range(h)]
    if cnt > 1:
        for c in range(w):
            i = h - 1
            for r in range(h-1, -1, -1):
                if ar[r][c]:
                    tmp[i][c] = ar[r][c]
                    i -= 1
        return tmp
    else: return ar

def copy(a):
    ret = [[0]*w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            ret[r][c] = a[r][c]
    return ret

def getcnt(ar):
    ans = 0
    for r in range(h):
        for c in range(w):
            if ar[r][c]:
                ans += 1
    return ans

def dfs(i, ar):
    global ans
    if i == n:
        ans = min(ans, getcnt(ar))
        return
    for iw in range(w):
        tmp = copy(ar)
        tmp = func(tmp, iw)
        dfs(i+1, tmp)

for t in range(int(input())):
    n, w, h = map(int, input().split())
    a = [list(map(int, input().split()))for _ in range(h)]
    ans = w*h
    dfs(0, a)
    print(f'#{t+1}', ans)
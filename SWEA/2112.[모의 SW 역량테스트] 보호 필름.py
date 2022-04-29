def isqualified():
    l = []
    for c in range(w):
        cnt = 1
        tag = False
        for r in range(1, d):
            if a[r][c] == a[r-1][c]:
                cnt += 1
            else: cnt = 1
            if cnt >= k:
                tag = True
        if not tag: return False
    return True


def dfs(cnt, n):
    global ans
    if cnt > ans: return
    if isqualified():
        ans = min(ans, cnt)
        return
    for i in range(n, d):
        tmp = a[i]
        for c in [0,1]:
            a[i] = [c]*w
            dfs(cnt+1, i+1)
        a[i] = tmp

for t in range(int(input())):
    d, w, k = map(int, input().split())
    a = [list(map(int, input().split()))for _ in range(d)]
    ans = k
    dfs(0, 0)
    print(f'#{t+1}',ans)

def isconnectable(r, c, d):
    r, c = r + dr[d], c + dc[d]
    l = 0
    while 0 <= r < N and 0 <= c < N:
        if A[r][c] != 0:
            return 0
        l += 1
        r, c = r + dr[d], c + dc[d]
    return l


def connect(r, c, d, flag):
    r, c = r + dr[d], c + dc[d]
    while 0 <= r < N and 0 <= c < N:
        A[r][c] = flag
        r, c = r+dr[d], c+dc[d]


def sol(i, n, a, ret, cnt):
    global ans
    global m_cnt
    while i < n*n and a[i//n][i%n]!=1:
        i += 1
    if i == n*n:
        if m_cnt < cnt:
            ans = ret
        m_cnt = max(cnt, m_cnt)
        if cnt == m_cnt:
            ans = min(ret, ans)
        return
    r, c = i//n, i%n
    if r == 0 or r == n-1 or c == 0 or c == n-1:
        sol(i+1, n, a, ret, cnt+1)
        return

    sol(i+1, n, a, ret, cnt)
    for d in range(4):
        l = isconnectable(r, c, d)
        if l:
            connect(r, c, d, 2)
            sol(i+1, n, a, ret+l, cnt+1)
            connect(r, c, d, 0)



dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
for t in range(int(input())):
    N = int(input())
    A = [list(map(int, input().split()))for _ in range(N)]
    ans = 9999
    m_cnt = 0
    sol(0, N,  A, 0, 0)
    print(f'#{ t +1}', ans)

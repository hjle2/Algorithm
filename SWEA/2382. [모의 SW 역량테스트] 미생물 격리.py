dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def move():
    cal = [[[]for _ in range(n)]for _ in range(n)]
    for i in range(k):
        if not a[i]: continue
        r, c, s, d = a[i]
        nr, nc, nd = r + dr[d-1], c + dc[d-1], d
        if nr == 0:
            nd = 2
        elif nr == n-1:
            nd = 1
        elif nc == 0:
            nd = 4
        elif nc == n-1:
            nd = 3
        if nd != d:
            s = s//2
        a[i] = [nr, nc, s, nd]
        cal[nr][nc].append(i)

    for r in range(n):
        for c in range(n):
            if len(cal[r][c]) > 1:
                n_s = 0
                m_s = 0
                m_i = 0
                for i in cal[r][c]:
                    m_s = max(m_s, a[i][2])
                    if m_s == a[i][2]:
                        m_i = i
                for i in cal[r][c]:
                    if i != m_i:
                        n_s += a[i][2]
                        a[i] = []
                a[m_i][2] = n_s + m_s


def sol():
    for i in range(m):
        move()
    ans = 0
    for i in range(k):
        if a[i]:
           ans += a[i][2]
    return ans

for t in range(int(input())):
    n, m, k = map(int, input().split())
    a = [list(map(int, input().split()))for _ in range(k)]
    print(f'#{t+1}', sol())

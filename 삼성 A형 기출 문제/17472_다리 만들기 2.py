from collections import deque
def connect(a, b):
    a, b = getparent(a), getparent(b)
    conn[max(a,b)] = min(a,b)

def getparent(a):
    if conn[a] == a: return a
    return getparent(conn[a])


def getbridgelen(a, b):
    v = [[False]*M for _ in range(N)]
    r, c = pt[a]
    v[r][c] = True
    q = deque([(r, c)])
    m_len = 10
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0<=nr<N and 0<=nc<M:
                if not v[nr][nc] and A[nr][nc] == a+1:
                    v[nr][nc] = True
                    q.append((nr, nc))
                l = 0
                while 0<=nr<N and 0<=nc<M and A[nr][nc] == 0:
                    l += 1
                    nr, nc = nr+dr[i], nc+dc[i]
                if l>1 and 0<=nr<N and 0<=nc<M and A[nr][nc] == b+1:
                    m_len = min(m_len, l)
    return m_len if m_len < 10 else 0


def indexing(r, c, n):
    q = deque([(r, c)])
    v[r][c] = True
    A[r][c] = n
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0<=nr<N and 0<=nc<M and not v[nr][nc] and A[nr][nc]:
                v[nr][nc] = True
                A[nr][nc] = n
                q.append((nr, nc))


N, M = map(int, input().split())
A = [list(map(int, input().split()))for _ in range(N)]
v = [[False]*M for _ in range(N)]
dr = [-1,1,0,0]
dc = [0,0,-1,1]
pt = []

n = 0
for r in range(N):
    for c in range(M):
        if not v[r][c] and A[r][c]:
            n += 1
            indexing(r, c, n)
            pt.append((r, c))

bridge_len = []
for i in range(n-1):
    for j in range(i+1, n):
        ret = getbridgelen(i, j)
        if ret > 1: bridge_len.append((i, j, ret))

conn = [i for i in range(n)]
bridge_len.sort(key=lambda x:x[2])
ans = 0
while bridge_len:
    a, b, l = bridge_len.pop(0)
    if getparent(a) != getparent(b):
        connect(a,b)
        ans += l

for i in range(n):
    if getparent(i) != 0:
        ans = -1
        break
print(ans)
from copy import deepcopy
def hunt(ar, h):
    for d in range(1, D+1):
        for i in range(-d, d+1):
            r, c = N-(d-abs(i)), h+i
            if 0<=r<N and 0<=c<M and ar[r][c]:
                return (r, c)

def sol(H):
    ar = deepcopy(A)
    c_h = 0
    for _ in range(N):
        ret = []
        for h in H:
            r = hunt(ar,  h)
            if r: ret.append(r)
        for r, c in ret:
            if ar[r][c]:
                c_h += 1
                ar[r][c] = 0
        ar.pop()
        ar.insert(0, [0]*M)
    return c_h


N, M, D = map(int, input().split())
A = [list(map(int, input().split()))for _ in range(N)]
print(max(sol([i,j,k])for i in range(M-2) for j in range(i+1, M-1) for k in range(j+1, M)))

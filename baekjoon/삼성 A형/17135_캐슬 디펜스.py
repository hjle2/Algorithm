from copy import deepcopy


def turn(n, m, a, hh, d):
    cnt = 0
    for _ in range(n):
        ret = []
        for h in hh:
            r = hunt(n, m, h, d, a)
            if r: ret.append(r)
        for r, c in ret:
            if a[r][c]:
               cnt += 1
               a[r][c] = 0
        a.pop()
        a.insert(0, [0]*m)
    return cnt

def hunt(n, m, h, dd, a):
    for d in range(1, dd+1):
        for x in range(-d, d+1):
            r, c = n-(d-abs(x)), h+x
            if 0<=r<n and 0<=c<m and a[r][c]:
                return (r, c)


def sol(n, m, d, a):
    ans = 0
    for i in range(m-2):
        for j in range(i+1, m-1):
            for k in range(j+1, m):
                ans = max(ans, turn(n, m, deepcopy(a), [i,j,k], d))
    return ans

n, m, d = map(int, input().split())
a = [list(map(int, input().split()))for _ in range(n)]
print(sol(n, m, d, a))

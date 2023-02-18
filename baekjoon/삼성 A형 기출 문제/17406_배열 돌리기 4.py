from copy import deepcopy


def rotate(ar, r, c, s):
    for i_s in range(1, s+1):
        fr, fc = r-i_s, c-i_s
        er, ec = r+i_s, c+i_s
        first = ar[fr][fc]
        for x in range(fr, er):
            ar[x][fc] = ar[x+1][fc]
        for x in range(fc, ec):
            ar[er][x] = ar[er][x+1]
        for x in range(er, fr, -1):
            ar[x][ec] = ar[x-1][ec]
        for x in range(ec, fc, -1):
            ar[fr][x] = ar[fr][x-1]
        ar[fr][fc+1] = first


def make_case(n, q):
    global ans
    if n == 0:
        ar = deepcopy(A)
        for i in q:
            r, c, s = lst_r[i]
            rotate(ar, r-1, c-1, s)
        ans = min(ans, min(sum(ar[i])for i in range(N)))
        return
    for i in range(K):
        if i not in q:
            make_case(n-1, q+[i])


N, M, K = map(int, input().split())
A = [list(map(int, input().split()))for _ in range(N)]
lst_r = [list(map(int, input().split()))for _ in range(K)]

ans = 999999
make_case(K, [])
print(ans if ans < 999999 else -1)
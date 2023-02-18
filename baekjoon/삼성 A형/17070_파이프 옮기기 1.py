def sol(n, a):
    ar = [[[0]*3 for _ in range(n)]for _ in range(n)]
    ar[0][1][0] = 1
    for r in range(n):
        for c in range(2, n):
            if a[r][c]: continue
            ar[r][c][0] = sum(ar[r][c-1][:2])
            if r>0:
                ar[r][c][2] = sum(ar[r-1][c][1:])
                if a[r-1][c]==0 and a[r][c-1]==0:
                    ar[r][c][1] = sum(ar[r-1][c-1])
    return sum(ar[n-1][n-1])

n = int(input())
a = [list(map(int, input().split()))for _ in range(n)]
print(sol(n, a))

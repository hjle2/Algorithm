N = int(input())
A = [list(map(int, input().split()))for _ in range(N)]
ar = [[[0]*3 for _ in range(N)] for _ in range(N)]
ar[0][1][0] = 1

for r in range(N):
    for c in range(2, N):
        if A[r][c]: continue
        ar[r][c][0] = sum(ar[r][c-1][:2])
        if r > 0:
            if not A[r-1][c] and not A[r][c-1]:
                ar[r][c][1] = sum(ar[r-1][c-1])
            ar[r][c][2] = sum(ar[r-1][c][1:])
print(sum(ar[N-1][N-1]))

def solve(A, B):
    L = A[:]
    cnt = 0
    for i in range(1, n):
        if L[i-1] == B[i-1]:
            continue
        cnt += 1

        for j in range(i-1, i+2):
            if j < n:
                L[j] = 1 - L[j]
    return cnt if L == B else 1e9


n = int(input())
a = [*map(int, input())]
b = [*map(int, input())]

ans = solve(a, b)
a[0] = 1-a[0]
a[1] = 1-a[1]
ans = min(ans, solve(a, b) + 1)
print(ans if ans != 1e9 else -1)
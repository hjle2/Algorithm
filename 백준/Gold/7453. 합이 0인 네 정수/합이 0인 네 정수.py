def solve():
    ans = 0
    l, r = 0, n * n - 1
    while l < n * n and 0 <= r:
        tmp = ab[l] + cd[r]
        if tmp == 0:
            i, j = l + 1, r - 1
            while i < n*n and ab[l] == ab[i]:
                i += 1
            while 0 <= j and cd[r] == cd[j]:
                j -= 1
            ans += (i - l) * (r - j)
            l, r = i, j
        elif tmp > 0:
            r -= 1
        else:
            l += 1
    print(ans)


n = int(input())
ar = [[*map(int, input().split())]for _ in range(n)]
ab, cd = [], []
for i in range(n):
    for j in range(n):
        ab.append(ar[i][0] + ar[j][1])
        cd.append(ar[i][2] + ar[j][3])
ab.sort()
cd.sort()
solve()
n = int(input())
ar = [*map(int, input().split())]
x = int(input())

ar.sort()
ans = 0
for a in range(n-1):
    l, r = a+1, n-1
    a = ar[a]
    while l <= r:
        m = (l + r) // 2
        b = ar[m]
        tmp = a + b
        if tmp == x:
            break
        elif tmp < x:
            l = m + 1
        else:
            r = m - 1
    if tmp == x:
        ans += 1
print(ans)
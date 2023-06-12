n, m = map(int, input().split())
ar = sorted([int(input()) for _ in range(n)])

ans = ar[-1] - ar[0]
l, r = 0, 1
while l < n and r < n:
    diff = ar[r] - ar[l]
    if diff < m:
        r += 1
    else:
        l += 1
        ans = min(ans, diff)
        if diff == m:
            break
print(ans)
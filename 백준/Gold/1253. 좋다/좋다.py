def is_good(i, num):
    l, r = 0, n-1
    if l == i:
        l += 1
    if r == i:
        r -= 1
    tmp = 2000000001
    while l < r:
        tmp = ar[l] + ar[r]
        if tmp < num:
            l += 1
            if l == i:
                l += 1
        else:
            if tmp == num:
                break
            r -= 1
            if r == i:
                r -= 1
    if tmp == num:
        return True
    return False


n = int(input())
ar = sorted([*map(int, input().split())])

ans = 0
for i in range(n):
    if is_good(i, ar[i]):
        ans += 1
print(ans)


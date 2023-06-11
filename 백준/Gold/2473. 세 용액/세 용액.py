n = int(input())
ar = sorted([*map(int, input().split())])

ans = []
min_diff = 3000000001

for m in range(1, n-1):
    l, r = 0, n-1

    while l < m < r:
        tmp = ar[l] + ar[m] + ar[r]
        if abs(tmp) < min_diff:
            min_diff = abs(tmp)
            ans = [ar[l], ar[m], ar[r]]
            if min_diff == 0:
                break

        if tmp < 0:
            l += 1
        else:
            r -= 1
    if min_diff == 0:
        break

print(*sorted(ans))
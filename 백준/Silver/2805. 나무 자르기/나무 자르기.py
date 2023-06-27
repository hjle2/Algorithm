def get_length(m):
    ret = 0
    for i, height in enumerate(ar):
        if height - m > 0:
           ret += height - m
    return ret


n, m = map(int, input().split())
ar = [*map(int, input().split())]

l, r = 0, max(ar)
ans = 0
while l <= r:
    mid = (l + r) // 2
    tmp = get_length(mid)
    if tmp >= m:
        ans = max(ans, mid)
        l = mid + 1
    else:
        r = mid - 1
print(ans)
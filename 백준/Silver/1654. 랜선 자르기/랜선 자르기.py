def get_total_cnt(m):
    cnt = 0
    for i, length in enumerate(ar):
        cnt += length // m
    return cnt


k, n = map(int, input().split())
ar = [int(input()) for _ in range(k)]

l, r = 1, max(ar)
ans = 0
while l <= r:
    m = (l + r) // 2
    cnt = get_total_cnt(m)

    if cnt < n:
        r = m - 1
    else:
        ans = max(ans, m)
        l = m + 1
print(ans)
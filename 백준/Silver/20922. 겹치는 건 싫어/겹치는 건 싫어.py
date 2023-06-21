n, k = map(int, input().split())
ar = [*map(int, input().split())]

cnt_ar = [0] * (max(ar) + 1)

s, e = 0, 0
ans = 0
while e < n:
    if cnt_ar[ar[e]] < k:
        cnt_ar[ar[e]] += 1
        e += 1
    else:
        cnt_ar[ar[s]] -= 1
        s += 1
    ans = max(ans, e - s)
print(ans)
n = int(input())
ar = [*map(int, input().split())]
cnt_ar = [0] * (max(ar) + 1)
s, e = 0, 0
ans = 0
while s < n and e < n:
    if cnt_ar[ar[e]] == 0:
        cnt_ar[ar[e]] += 1
        e += 1
        ans += e - s
    else:
        cnt_ar[ar[s]] -= 1
        s += 1
print(ans)
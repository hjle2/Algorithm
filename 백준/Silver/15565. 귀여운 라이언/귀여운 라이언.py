import sys
input = sys.stdin.readline
n, k = map(int, input().split())
ar = [*map(int, input().split())]
lion_cnt = 0
l, r = 0, 0
if ar[0] == 1:
    lion_cnt += 1
ans = 10 ** 6 + 1
while r < n:
    if lion_cnt < k:
        r += 1
        if r < n and ar[r] == 1:
            lion_cnt += 1
    else:
        ans = min(ans, r - l + 1)
        if ar[l] == 1:
            lion_cnt -= 1
        l += 1
print(ans if ans < 10 ** 6 + 1 else -1)

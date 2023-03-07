import sys
input = sys.stdin.readline

cnt = [0] * 26
val = [0] * 26

n = int(input())
nums = [[*input().strip()]for _ in range(n)]
oa = ord('A')

for num in nums:
    digit = 10 ** (len(num)-1)
    for c in num:
        cnt[ord(c) - oa] += digit
        digit //= 10

for v in range(9, -1, -1):
    max_idx = -1
    max_cnt = 0
    for i, c in enumerate(cnt):
        if max_cnt < c:
            max_idx, max_cnt = i, c
    if max_idx == -1:
        break
    cnt[max_idx] = -1
    val[max_idx] = v

ans = 0
for num in nums:
    digit = 10 ** (len(num)-1)
    for c in num:
        ans += val[ord(c) - oa] * digit
        digit //= 10
print(ans)
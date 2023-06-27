import sys
from collections import Counter

n = int(sys.stdin.readline())
ar = [*map(int, sys.stdin.readline().split())]
ar.sort()
ar_cnt = Counter(ar)

ans = 0
for i, a in enumerate(ar):
    l, r = i+1, n-1
    while l < r:
        # 같은 값이 있는 경우에 대한 처리 필요
        tmp = a + ar[l] + ar[r]
        if tmp == 0:
            if ar[l] == ar[r]:
                ans += r - l
            else:
                ans += ar_cnt[ar[r]]
            l += 1
        elif tmp < 0:
            l += 1
        else:
            r -= 1
print(ans)
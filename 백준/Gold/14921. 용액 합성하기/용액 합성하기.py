import sys
input = sys.stdin.readline
n = int(input())
ar = [*map(int, input().split())]
ar.sort()

s, e = 0, n-1
ret = 200000001
ans = 0
while s < e:
    tmp = ar[s] + ar[e]
    if tmp == 0:
        ans = 0
        break
    elif tmp < 0:
        s += 1
    elif tmp > 0:
        e -= 1
    if ret > abs(tmp):
        ret = abs(tmp)
        ans = tmp
print(ans)
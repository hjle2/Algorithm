import sys
input = sys.stdin.readline
N = int(input())
plus = []
minus = []
zeroCnt = 0
for _ in range(N):
    n = int(input())
    if n < 0:
        minus.append(n)
    elif n > 0:
        plus.append(n)
    else:
        zeroCnt = 1

plus.sort(reverse=True)
minus.sort()

ans = 0
while plus:
    x = plus.pop(0)
    if plus:
        y = plus.pop(0)
        if x * y > x + y:
            ans += x * y
        else:
            ans += x + y
    else:
        ans += x
while minus:
    x = minus.pop(0)
    if minus:
        y = minus.pop(0)
        ans += x * y
    else:
        if not zeroCnt:
            ans += x
print(ans)
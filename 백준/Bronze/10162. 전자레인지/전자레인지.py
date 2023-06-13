a = 60 * 5
b = 60
c = 10

n = int(input())
ans = [0] * 3
if n >= a:
    ans[0] = n // a
    n -= ans[0] * a
if n >= b:
    ans[1] = n // b
    n -= ans[1] * b
if n >= c:
    ans[2] = n // c
    n -= ans[2] * c
if n == 0:
    print(*ans)
else:
    print(-1)
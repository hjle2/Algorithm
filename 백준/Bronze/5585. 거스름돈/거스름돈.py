n = int(input())
n = 1000 - n

ans = 0
if n >= 500:
    ans += 1
    n -= 500
if n >= 100:
    ans += n // 100
    n = n % 100
if n >= 50:
    ans += 1
    n -= 50
if n >= 10:
    ans += n // 10
    n = n % 10
if n >= 5:
    ans += 1
    n -= 5
if n > 0:
    ans += n
print(ans)
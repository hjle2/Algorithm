n, m = map(int, input().split())
six_price = 1e9
one_price = 1e9
for _ in range(m):
    six, one = map(int, input().split())
    six_price = min(six_price, six)
    one_price = min(one_price, one)

ans = 1e9
if six_price >= one_price * 6:
    ans = one_price * n
else:
    ans = six_price * (n // 6) + one_price * (n - n // 6 * 6)
    ans = min(ans, six_price * (n // 6 + 1))
print(ans)
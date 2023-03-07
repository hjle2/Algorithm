n = 1000 - int(input())
coin = [500, 100, 50, 10, 5, 1]

cnt = 0
for i in coin:
    if n >= i:
        cnt += n // i
        n = n % i
print(cnt)
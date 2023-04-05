n = int(input())
train = [0] * n
for i in range(n):
    pt, speed = map(int, input().split())
    train[n-1-i] = speed

head = train[0]
ans = 1
for i in range(1, n):
    if head >= train[i]:
        ans += 1
        head = train[i]

print(ans)

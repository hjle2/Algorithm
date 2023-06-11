n, m = map(int, input().split())
ar = [*map(int, input().split())]

s = [0] * (n+1)                 # 누적합을 계산해 둔 배열
for i in range(1, n+1):
    s[i] = s[i-1] + ar[i-1]

ans = 0

for i in range(n):
    for j in range(i, n):
        tmp = s[j+1] - s[i]
        if tmp == m:
            ans += 1
            break
print(ans)
n, l = map(int, input().split())
spot = sorted([*map(int, input().split())])
dist = [0] * (n-1)

for i in range(1, n):
    dist[i-1] = spot[i] - spot[i-1]

tape = l
ans = 1
for d in dist:
    if d < tape:
       tape -= d
    else:
        ans += 1
        tape = l
print(ans)

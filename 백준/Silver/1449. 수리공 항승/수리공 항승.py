n, l = map(int, input().split())
spot = [*map(int, input().split())]
spot.sort()

ans, end = 0, 0
for s in spot:
    if end < s:
        ans += 1
        end = s + l - 1
print(ans)
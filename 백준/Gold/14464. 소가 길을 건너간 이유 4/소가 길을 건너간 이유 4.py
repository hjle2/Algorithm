import sys
input = sys.stdin.readline

c, n = map(int, input().split())
t = [int(input()) for _ in range(c)]
ab = [[*map(int, input().split())]for _ in range(n)]
ab.sort(key=lambda x:(x[1], x[0]))
t.sort()

v = [False] * c
ans = 0
for a, b in ab:
    for i, tt in enumerate(t):
        if a <= tt <= b and not v[i]:
            ans += 1
            v[i] = True
            break
print(ans)
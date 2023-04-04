n, a, b = map(int, input().split())
ans = b - a + 1

num = []
for _ in range(n):
    s, p = input().split()
    if s == 'NS':
        ans -= 1
    p = int(p)
    num.append([p, s])
num.sort()


import sys
input = sys.stdin.readline


n = int(input())
l = sorted([int(input()) for _ in range(n)])
ans = 0
for i, li in enumerate(l):
    ans = max(ans, (n - i) * li)
print(ans)
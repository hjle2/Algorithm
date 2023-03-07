import sys
si = sys.stdin.readline

n = int(input())
a = sorted([*map(int, input().split())])
b = sorted([*map(int, input().split())], reverse=True)

ans = 0
for i in range(n):
    ans += a[i] * b[i]
print(ans)
import sys
input = sys.stdin.readline

# n의 max 는 10000
d = [0] * 10001
for i in range(1, int(input())+1):
    d[i], *a = map(int, input().split())
    if a[0] > 0:
        d[i] += max(d[j]for j in a[1:])
print(max(d))
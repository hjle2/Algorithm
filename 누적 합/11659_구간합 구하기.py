import sys

input = sys.stdin.readline
N, M = map(int, input().split())
ar = [0] + [*map(int, input().split())]
sum = [0] * (N+1)
for i in range(1, N+1):
    sum[i] = sum[i-1] + ar[i]

for i in range(M):
    s, e = map(int, input().split())
    print(sum[e] - sum[s-1])
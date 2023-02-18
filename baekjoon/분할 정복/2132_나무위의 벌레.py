import sys

input = sys.stdin.readline
N = int(input())
C = [*map(int, input().split())]
A = [[]for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    A[a-1].append(b-1)
    A[b-1].append(a-1)


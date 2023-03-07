import sys
input = sys.stdin.readline

n = sorted([*map(int, input().strip())], reverse=True)
if sum(n) % 3 or n[-1] != 0:
    print(-1)
else:
    print(*n, sep='')

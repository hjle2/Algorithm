import sys

input = sys.stdin.readline
N = int(input())
map = [int(input())for _ in range(N)]
map.sort()
print(*map, sep='\n')
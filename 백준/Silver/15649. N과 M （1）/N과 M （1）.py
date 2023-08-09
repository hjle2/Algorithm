import itertools

n, m = map(int, input().split())
for a in itertools.permutations([*range(1, n+1)], m):
    print(*a)
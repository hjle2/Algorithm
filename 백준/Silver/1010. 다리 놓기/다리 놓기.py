import itertools

for _ in range(int(input())):
    n, m = map(int, input().split())
    tmp = 1
    for i in range(1, m+1):
        tmp *= i
    for i in range(1, m-n+1):
        tmp //= i
    for i in range(1, m-m+n+1):
        tmp //= i
    print(tmp)
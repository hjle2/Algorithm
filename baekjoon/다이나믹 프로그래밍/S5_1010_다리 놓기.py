from math import factorial

def solve(n, m):
    return factorial(m) // factorial(n) // factorial(m-n)

for _ in range(int(input())):
    N, M = map(int, input().split())
    print(solve(N, M))
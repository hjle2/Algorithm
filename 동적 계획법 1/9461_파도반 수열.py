def solve(n):
    for t in range(i, n+1):
        P[t] = P[t-5] + P[t-1]
    return P[n]


P = [0] * 101
P[1:11] = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
i = 11
for _ in range(int(input())):
    n = int(input())
    if n >= i:
        print(solve(n))
        i = n
    else:
        print(P[n])
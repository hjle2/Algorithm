def solve(s):
    if n == 1:
        print(1)
        return
    for i in range(1, n+1):
        if s + i > n:
            break
        s += i
    print(i-1)

n = int(input())
s = 0
solve(s)
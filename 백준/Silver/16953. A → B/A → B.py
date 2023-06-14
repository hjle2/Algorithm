def solve(a, b):
    ans = 0
    while a < b:
        if not b % 2:
            b //= 2
        elif b % 10 == 1:
            b -= 1
            b //= 10
        else:
            print(-1)
            return
        ans += 1
    print(ans + 1 if a == b else -1)


a, b = map(int, input().split())
solve(a, b)
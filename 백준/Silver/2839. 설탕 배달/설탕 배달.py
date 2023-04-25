n = int(input())

def solve(n):
    if n == 4 or n == 7:
        return -1
    ans = 0
    while n % 5:
        ans += 1
        n -= 3
    return ans + n // 5

print(solve(n))
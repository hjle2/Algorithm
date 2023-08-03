n = int(input())

def solve():
    five = n // 5
    for i in range(five, -1, -1):
        tmp = n - 5 * i
        if tmp % 2 == 0:
            print(i + tmp // 2)
            return
    print(-1)
    return

solve()
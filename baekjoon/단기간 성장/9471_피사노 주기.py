
N = int(input())
A = []
for _ in range(N):
    a, b = map(int, input().split())
    if b == 2: print(a, 3)
    else:
        n = 2
        a1, a2 = 1, 2
        while True:
            a1, a2 = a2 % b, (a1 + a2) % b
            if a1 == 1 and a2 == 1:
                break
            n += 1
        print(a, n)

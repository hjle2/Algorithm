def pibo_period():
    n = 2
    a1, a2 = 1, 2
    while True:
        a1, a2 = a2 % p, (a1 + a2) % p
        if a1 == 1 and a2 == 1:
            break
        n += 1
    return n

def pibonacci(a):
    a0, a1 = 1, 1
    n = 2
    while n < a:
        a0, a1 = a1 % p, (a0 + a1) % p
        n += 1
    return a1


N = int(input())
p = 1000000
period = pibo_period()
print(period)
N %= period
print(pibonacci(N))

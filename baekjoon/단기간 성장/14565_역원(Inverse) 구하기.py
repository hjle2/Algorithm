def gcd(a, b):
    return gcd(b, a%b) if b else a

def xgcd(a, b):
    r0, r1 = a, b
    s0, s1 = 1, 0
    t0, t1 = 0, 1

    while True:
        q = r0 // r1
        r = r0 - q * r1
        s = s0 - q * s1
        t = t0 - q * t1
        if r == 0:
            return s1
        r0, r1 = r1, r
        s0, s1 = s1, s
        t0, t1 = t1, t


N, A = map(int, input().split())
if gcd(A, N) != 1:
    inv = -1
else:
    inv = xgcd(A, N)
    while inv <= 0:
        inv += N
print(N-A, inv)
# 1. 나눗셈 연산에는 모듈러 연산의 분배법칙이 성립하지 않는다.
# 2. 페르마의 소정리
# a는 정수, p는 소수이며, a가 p의 배수가 아닐 때
# a^p = a mod p
# a^-1 mode p 는 a^p-2이 되기 때문에 곱셉에 대한 모듈러 연산의 분배법칙이 석립된다
# 하지만, p가 너무너무 크기 때문에 분할정복으로 곱셈값을 계산한다!

n, k = map(int, input().split())
p = 1000000007


# 반복문 방식
def power1(base, expo):
    ret = 1
    while expo:
        if expo % 2 == 1:
            ret = ret * base % p
        base = base * base % p
        expo //= 2
    return ret


# 재귀 방식
def power2(base, expo):
    if expo == 1:
        return base % p

    tmp = power2(base, expo // 2)

    if expo % 2 == 1:
        return tmp * tmp * base % p
    else:
        return tmp * tmp % p


fact = [1] * (n+1)
for i in range(2, n+1):
    fact[i] = fact[i-1] * i % p
print(fact[n] * power2(fact[k] * fact[n-k], p-2) % p)
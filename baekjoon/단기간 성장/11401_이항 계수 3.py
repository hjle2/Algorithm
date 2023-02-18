from math import factorial

n, k = map(int, input().split())
ans = factorial(k) * factorial(n-k)
ans = factorial(n) // ans
print(ans%1000000007)

# 페르마의 소정리 (p소수, a정수)
# 소수가 아닌 수도 있음 이를 카마이클 수 라고 부른다.
# p가 소수이고, a 가 p의 배수가 아닐 떄
# a^p 를 p로 나눈 나머지는 a
# 즉, a ^ (p-1) 을 p로 나눈 나머지는 1이다.
# 또, a ^ (p-2) 을 p로 나눈 나머지는 a^(-1) -> 이를 이용한다.

# 확장 유클리드 호제법
# 유클리드 호제법은 두 정수 사이의 최대 공약수를 효과적으로 구하는 방법으로
# 다음 식을 만족하는 방법론을 일컫는 말이다.
# GCD(A, B) = GCD(B, r)
# A > B, A 를 B 로 나눈 나머지를 r

# 확장 유클리드 호제법을 공부하기 위해선 베주 항등식을 알아야 한다.
# GCD(a, b) = d라고 할 때
# ax + by = d를 만족하는 정수 x, y 가 존재한다.
# d는 정수 x, y 에 대해 ax + by 로 표현 가능한 가장 작은 정수이다.
# ax + by 로 표현가능 한 정수는 d의 배수이다.

# 확장 유클리드 호제법
# 베주 항등식과 유클리드 호제법을 이용하여 해를 구하는 방법
# 모듈러 연산에서의 곱셈의 역원이 확장 유클리드 호제법을 잘 이용할 수 있는 대표적 예


# 분할정복
# 문제를 나눌 수 없을 때까지 나누어 각각 풀고, 다시 합병하여 답을 얻는 알고리즘
# 분할 가능한 경우 2개 이상의 문제로 나눈다
# 분할이 가능하면 또 다시 나눈다. 그렇지 않으면 문제 풀기
# 문제들을 통합하여 원래의 답을 얻는다.

# 분할정복 알고리즘 이용
def power(a, b):
    if b == 0:
        return 1
    if b % 2:
        return (power(a, b // 2) ** 2 * a) % p
    else:
        return (power(a, b // 2) ** 2) % p


p = 1000000007
N, K = map(int, input().split())

fact = [1 for _ in range(N + 1)]

for i in range(2, N + 1):
    fact[i] = fact[i - 1] * i % p

A = fact[N]
B = fact[N - K] * fact[K]

# 페르마의 소정리 이용
print(A * power(B, p - 2) % p)
import math


def isprime(n):
    if n == 1: return False
    if n == 2: return True
    v = int(math.sqrt(n)) + 1
    for i in range(2, v):
        if n%i==0: return False
    return True
    # if n == 1: return False
    # elif n == 2: return True
    # v = int(math.sqrt(n)) + 1
    # ar = [False]*v
    # for i in range(2, v):
    #     k = i
    #     if not ar[i]:
    #         while k<=n:
    #             if k == n:
    #                 return False
    #             if k < v:
    #                 ar[k] = True
    #             k += i
    # return True
    # if n == 1: return False
    # elif n == 2: return True
    # for i in range(2, n):
    #     if i%n == 0:
    #         return False
    # return True

def xnary(n, k):
    ans = ''
    while n > 0:
        ans = str(n%k) + ans
        n //= k
    return ans

def solution(n, k):
    answer = 0
    nary = xnary(n, k).split('0')
    for i in nary:
        if i and isprime(int(i)):
            answer += 1
    return answer

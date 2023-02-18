# 길이가 N 인 수열에서 수열의 합을 구하고자 한다
# 수열의 두 수를 위치에 상관없이 묶어 묶은 수는 곱한 후 더한다
# 모든 수는 한번 묶어나 묶지 않아야 한다
# 그 합의 최대를 구하라

import sys
input = sys.stdin.readline
N = int(input())
# plus = []
# minus = []
# zeroCnt = 0
# for _ in range(N):
#     n = int(input())
#     if n < 0:
#         minus.append(n)
#     elif n > 0:
#         plus.append(n)
#     else:
#         zeroCnt = 1
#
# plus.sort(reverse=True)
# minus.sort()
#
# ans = 0
# while plus:
#     x = plus.pop(0)
#     if plus:
#         y = plus.pop(0)
#         if x * y > x + y:
#             ans += x * y
#         else:
#             ans += x + y
#     else:
#         ans += x
# while minus:
#     x = minus.pop(0)
#     if minus:
#         y = minus.pop(0)
#         ans += x * y
#     else:
#         if not zeroCnt:
#             ans += x
# print(ans)

A = [int(input())for _ in range(N)]
A.sort()
ans = 0
i, j = -1, N
while i + 2 < N and A[i+2] <= 0:
    ans += A[i+1] * A[i+2]
    i += 2
while j > 1 and A[j-2] > 1:
    ans += A[j-1] * A[j-2]
    j -= 2
ans += A[i+1:j]
print(ans)
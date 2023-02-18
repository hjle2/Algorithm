# 함수 S는 A[0] * B[0] ~ + A[N-1] * B[N-1] 이다
# S의 값을 가장 작게 만들기 위해 A의 수를 재배열 해야 한다
# 단, B는 재배열 하면 안된다
# S의 최솟값을 구하라

import sys
input = sys.stdin.readline
N = int(input())
A = [*map(int, input().split())]
B = [*map(int, input().split())]
A.sort(reverse=1)
B.sort()
ans = 0
for i in range(N):
    ans += A[i] * B[i]
print(ans)
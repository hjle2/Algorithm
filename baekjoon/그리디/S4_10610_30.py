# 수에 포함된 숫자들을 섞어 30의 배수가 되는 가장 큰 수를 만들어야 한다

import sys
input = sys.stdin.readline

def solve():
    if cnt[0] == 0:
        return -1
    digit = 0
    for i in range(10):
        digit += cnt[i] * i
    if digit % 3 == 0:
        ans = 0
        for i in range(9, -1, -1):
            for _ in range(cnt[i]):
                ans *= 10
                ans += i
        return ans
    else:
        return -1
        
N = [*input()]
cnt = [0] * 10
for n in N:
    if n in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        cnt[int(n)] += 1
print(solve())
# input 에 함정이 있었나 보다

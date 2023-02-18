# 수학 문제를 푸는 숙제가 있다
# 1. 수학 문제는 N개의 단어로 이루어져 있다
# 2 각 단어는 알파벳 대문자로 이루어져 있다
# 3. 각 알파벳 대문자를 0-9 숫자로 바꿔 N개의 수의 합을 구한다
# N 개의 단어가 주어졌을 때 그 수의 합을 최대로 만드는 프로그램을 작성하라
import sys
input = sys.stdin.readline

N = int(input())
alpha = [0] * 26
for _ in range(N):
    a = [*input()][:-1]
    n = len(a) - 1
    for l in a:
        alpha[ord(l) - 65] += 10 ** n
        n-=1
alpha.sort(reverse=True)
ans = 0
n = 9
for i in alpha:
    if i == 0: break
    ans += i * n
    n -= 1
print(ans)
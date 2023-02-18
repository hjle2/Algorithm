# 개미 여러마리가 길이가 lcm 인 막대 위에 있다
# 개미의 이동 속도는 일정 1 cm/s
# 막대의 마지막까지 걸어가면 '즉시' 떨어진다
# 두 개미가 만나면 방향을 반대로 바꾸어 걸어간다
# 처음 막대위의 개미 위치를 알고 있지만 방향은 모른다
# 모.든. 개미가 땅으로 떨어지는 가장 빠른 시간과 느린 시간을 구하라

# 막대의 길이와 개미의 수 n
# 개미의 초기 위치 n 개
# 모든 수는 <= 1.000.000

import sys
input = sys.stdin.readline

def main():
    cm, n = map(int, input().split())
    ant = [0] * n
    mint = 0
    maxt = 0
    for i in range(n):
        ant[i] = int(input())
        mint = max(mint, min(ant[i], cm - ant[i]))
        maxt = max(maxt, max(ant[i], cm - ant[i]))
    print(mint, maxt)
for _ in range(int(input())):
    main()
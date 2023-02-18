# N 개의 카드
# 1. x 번 카드와 y 번 카드를 골라 그 두 장에 쓰여진 수를 더한 값을 계산
# 2. 계산한 값을 x 번 카드와 y 번 카드에 덮어 쓴다
# 위의 과정을 m 번 하면 놀이가 끝난다
# n 장의 카드에 쓰인 수를 모두 더한 값이 점수
# 만들 수 있는 가장 작은 점수를 계산하는 프로그램을 만들자
import sys, heapq
input = sys.stdin.readline
N, M = map(int, input().split())
cards = [*map(int, input().split())]
heapq.heapify(cards)

for _ in range(M):
    a, b = heapq.heappop(cards), heapq.heappop(cards)
    v = a + b
    heapq.heappush(cards, v)
    heapq.heappush(cards, v)
print(sum(cards))
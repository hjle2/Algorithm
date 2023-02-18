# 보유한 숫자카드 N 개 중에서 정수 M 개 에 대해 몇 개 갖고 있는지 구하라
from collections import Counter


def find(x):
    l, r = 0, N-1
    while l <= r:
        m = (l+r)//2
        if cards[m] == x:
            return counter[x]
        if cards[m] < x:
            l =m+1
        else:
            r = m-1
    return 0


N = int(input())
cards = [*sorted(map(int, input().split()))]
counter = Counter(cards)
M = int(input())
nums = [*map(int, input().split())]

for x in nums:
    print(find(x), end=' ')

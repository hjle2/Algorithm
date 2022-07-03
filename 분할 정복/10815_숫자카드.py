# 점수 하나가 적혀있는 숫자 카드
# N개의 카드를 갖고 있고,
# 정수 M 개가 적혀 있는 숫자카드를 갖고 있는지 구하라

# N 1<=N<=500,000
# 카드의 수 -10,000,000 <= X <= 10,000,000
# 하나의 수는 하나의 카드에만 적혀 있다.

# M 1<=M<=500,000

def find(x):
    l, r = 0, N-1
    while l <= r:
        m = (l+r)//2
        if cards[m] == x:
            return True
        if cards[m] < x:
            l = m+1
        else:
            r = m-1
    return False


N = int(input())
cards = [*sorted(map(int, input().split()))]
M = int(input())
nums = [*map(int, input().split())]

for n in nums:
    print([0, 1][find(n)], end=' ')

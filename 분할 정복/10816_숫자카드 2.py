# 보유한 숫자카드 N 개 중에서 정수 M 개 에 대해 몇 개 갖고 있는지 구하라
def Count(x, i):
    l = r = i
    while l >= 0 and cards[l] == x:
        l -= 1
    while r < N and cards[r] == x:
        r += 1
    return r-l -1

def find(x):
    l, r = 0, N-1
    while l <= r:
        m = (l+r)//2
        if cards[m] == x:
            return Count(x, m)
        if cards[m] < x:
            l =m+1
        else:
            r = m-1
    return 0


N = int(input())
cards = [*sorted(map(int, input().split()))]
M = int(input())
nums = [*map(int, input().split())]

for x in nums:
    print(find(x), end=' ')

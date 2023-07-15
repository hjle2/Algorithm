def find(num):
    l, r = 0, n-1
    while l <= r:
        m = (l + r) // 2
        if cards[m] < num:
            l = m + 1
        elif cards[m] > num:
            r = m - 1
        else:
            return True
    return False


n = int(input())
cards = [*map(int, input().split())]
m = int(input())
nums = [*map(int, input().split())]

cards.sort()
for num in nums:
    if find(num):
        print(1, end=' ')
    else:
        print(0, end=' ')
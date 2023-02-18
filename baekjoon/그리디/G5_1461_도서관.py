# 현재 위치는 0
# 책들의 원래 위치가 주어질 때 책을 모두 제자리에 놔둘 때 드는 최소 걸음 수를 구하라
def getLast():
    if - book[0] > book[-1]:
        ans, i, m = book[0], 0, M
        while book and book[0] < 0 and m > 0:
            book.pop(0)
            m -= 1
        return -ans
    else:
        ans, i, m = book[-1], N-1, M
        while book and book[-1] > 0 and m > 0:
            book.pop()
            m -= 1
        return ans

N, M = map(int, input().split())
book = [*map(int, input().split())]
book.sort()
if N == 1:
    ans = book[0]
    book = []
else:
    ans = getLast()
while book:
    m = M
    if book[0] < 0:
        ans -= book[0] * 2
        while book and m > 0 and book[0] < 0:
            book.pop(0)
            m -= 1
    else:
        ans += book[-1] * 2
        while book and m > 0 and book[-1] > 0:
            book.pop()
            m -= 1
print(ans)


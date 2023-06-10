# 정수가 적힌 카드 N개를 갖고 있다.
# 정수 M개가 주어질 때 이 숫자가 적힌 카드를 상근이가 몇 개 갖고 있는지 구하라

# 상근이가 갖고 있는 카드의 개수
n = int(input())
# 상근이가 갖고 있는 카드에 적힌 정수
sang = sorted([*map(int, input().split())])


# 상근이가 몇 개 갖고 있는 숫자카드인지 구해야 할 개수
m = int(input())
cards = [*map(int, input().split())]


def find_start(card):
    s, e = 0, n-1
    while s <= e:
        mid = (s + e) // 2
        if sang[mid] < card:
            s = mid + 1
        else:
            e = mid - 1
    return e + 1 if e+1 < n and sang[e+1] == card else -1


def find_end(card):
    s, e = 0, n-1
    while s <= e:
        mid = (s + e) // 2
        if sang[mid] > card:
            e = mid - 1
        else:
            s = mid + 1
    return s - 1 if s >= 1 and sang[s-1] == card else -1


ans = []
for card in cards:
    s = find_start(card)
    if s == -1:
        ans.append(0)
    else:
        e = find_end(card)
        ans.append(e - s + 1)
print(*ans)

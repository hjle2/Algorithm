# 숫자를 눌러서 이동하는 경우
from collections import deque


def solve():
    que = deque([n])
    v = [False] * 1000000
    v[n] = True
    while que:
        cur = que.popleft()
        if is_possible(cur):
            return cur

        for nxt in [cur-1, cur+1]:
            if nxt < 0 or nxt > 999999 or v[nxt]: continue
            que.append(nxt)
            v[nxt] = True
    return


def is_possible(cur):
    number = [*map(int, [*str(cur).strip()])]
    for num in number:
        if broken[num]:
            return False
    return True


n = int(input())
m = int(input())
if m > 0:
    buttons = [*map(int, input().split())]
else:
    buttons = []
broken = [False] * 10
for button in buttons:
    broken[button] = True

ans = abs(100 - n)
if not all(broken):
    tmp = solve()
    ans = min(ans, len(str(tmp)) + abs(n - tmp))
print(ans)
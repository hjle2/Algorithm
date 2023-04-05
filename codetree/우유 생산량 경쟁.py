n = int(input()) # 기록의 수


def get_index(name):
    if name == 'Bessie':
        return 0
    elif name == 'Elsie':
        return 1
    elif name == 'Mildred':
        return 2


def is_changed(cow, value):
    global ans, cur
    production[cow] += value

    max_v = max(production)
    nxt = []
    for i in range(3):
        if production[i] == max_v:
            nxt.append(i)
    nxt = tuple(nxt)
    if cur != nxt:
        cur = nxt
        ans += 1


history = [[] for _ in range(n)]
for i in range(n):
    day, name, value = input().split()
    day = int(day)
    value = [*value]
    if value[0] == '+':
        value = int(value[1])
    else:
        value = -int(value[1])
    history[i] = [day, get_index(name), value]
history.sort()

production = [7] * 3
cur = (0, 1, 2)
ans = 0

for i in range(n):
    day, cow, value = history[i]
    is_changed(cow, value)
print(ans)

a, b = map(int, input().split())
v = [-1] * 100001

que = [a]
v[a] = 0
while a != b:
    a = que.pop(0)
    if a-1 >= 0 and v[a-1] == -1:
        v[a-1] = v[a] + 1
        que.append(a-1)
    if a+1 <= 100000 and v[a+1] == -1:
        v[a+1] = v[a] + 1
        que.append(a+1)
    if a * 2 <= 100000 and v[a*2] == -1:
        v[a * 2] = v[a] + 1
        que.append(a * 2)

print(v[b])
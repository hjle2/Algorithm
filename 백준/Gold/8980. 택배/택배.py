n, c = map(int, input().split())
m = int(input())
boxs = [[*map(int, input().split())]for _ in range(m)]
boxs.sort(key=lambda x:(x[1], x[0], x[2]))

truck = [0] * n
ans = 0
for i in range(m):
    frm, to, box_n = boxs[i]

    min_n = box_n
    for j in range(frm, to):
        min_n = min(min_n, c - truck[j])

    for j in range(frm, to):
        truck[j] += min_n

    ans += min_n
print(ans)
n, c = map(int, input().split())
m = int(input())

parcel = [[] for _ in range(m)]
for i in range(m):
    frm, to, box_n = map(int, input().split())
    parcel[i] = [frm, to, box_n]
parcel.sort()

truck = [0] * (n+1)

ans = 0
for i in range(m):
    frm, to, box_n = parcel[i]

    max_truck = 0
    for j in range(frm, to):
        max_truck = max(truck[j], max_truck)

    cap = min(box_n, c-max_truck) # 트럭에 실을 박스의 수

    for j in range(frm, to):
        truck[j] += cap

    ans += cap

print(ans)

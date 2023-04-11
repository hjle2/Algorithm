n, c = map(int, input().split())
m = int(input())

parcel = [[] for _ in range(m)]
for i in range(m):
    frm, to, box_n = map(int, input().split())
    parcel[i] = [frm, to, box_n]
parcel.sort(key=lambda x:x[1])

truck = [0] * n

ans = 0
for i in range(m):
    frm, to, box_n = parcel[i]
    truck_n = 0 # 트럭에 실을 박스의 수

    for j in range(frm, to): # from, to 구간에서 min 
        if truck_n <= max(truck[j], box_n):
            truck_n = max(truck[j], box_n)

    for j in range(frm, to):
        truck[j] += truck_n
    ans += truck_n

print(ans)

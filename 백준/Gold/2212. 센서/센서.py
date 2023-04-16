n = int(input())
k = int(input())
sensor = [*map(int, input().split())]
sensor.sort()

distance = []
for i in range(1, n):
    dist = sensor[i] - sensor[i-1]
    if dist:
        distance.append(dist)
distance.sort()
for i in range(k-1):
    if not distance: break
    distance.pop()
print(sum(distance))
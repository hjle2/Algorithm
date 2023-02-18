# 고속도로위에 N개의 센서가 있다
# 고속도로 위에 K개의 집중국을 세울 수 있다
# 집중국은 수신 가능 영역을 조절할 수 있는데, 고속도로 상 연결된 구간으로 나타난다
# N개의 센서가 적어도 하나의 집중국과 통신해야 한다
# 집중국의 수신 가능 영역 길이의 합을 최소화한 값을 구하라
def solve():
    if K >= N:
        return 0
    dist = []
    for i in range(1, N):
        # 센서 i 와 센서 i-1 사이의 거리
        dist.append(sensors[i] - sensors[i-1])
    dist.sort()
    for _ in range(K-1):
        dist.pop()
    return sum(dist)

N = int(input())
K = int(input())
sensors = sorted([*map(int, input().split())])
print(solve())

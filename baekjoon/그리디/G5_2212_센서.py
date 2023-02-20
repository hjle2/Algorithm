def solve():
    if n <= k: return 0 # 설치할 집중국이 모든 센서에 설치할 수 있을만큼 충분하다면 모든 집중국은 수신 가능 영역의 길이가 0이다

    dist = [0] * (n-1)
    for i in range(n-1):
        dist[i] = sensors[i+1] - sensors[i] # 모든 센서들의 수신 사이 거리를 구한다

    dist.sort(key=lambda x:-x) # 수신사이 거리가 긴 순으로 정렬하여 그 둘을 한번에 수신하지 않도록 분리한다
    return sum(dist[k-1:]) # k개 설치할 수 있다면 k개의 영역으로 쪼개어 k-1개의 가장 긴 거리를 수신하지 않도록 분리시킨다.

n = int(input())
k = int(input())

sensors = sorted([*map(int, input().split())])
print(solve())

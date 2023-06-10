import sys
input = sys.stdin.readline
# 집의 개수, 공유기의 개수
n, c = map(int, input().split())
house = sorted([int(input()) for _ in range(n)])


def binary_search():
    start, end = 1, house[-1] - house[0]    # 최소 거리 1, 최대 거리 end
    while start <= end:
        mid = (start + end) // 2

        cur = house[0]  # 무조건 0번째 집에 설치해야 하기 때문에!
        cnt = 1         # 공유기 설치 수

        for i in range(1, n):   # mid 간격으로 공유기를 설치했을 때 몇 개 설치할 수 있는 지 확인
            if house[i] >= cur + mid:
                cnt += 1
                cur = house[i]

        if cnt >= c:
            start = mid + 1
        else:
            end = mid - 1
    return start - 1

print(binary_search())
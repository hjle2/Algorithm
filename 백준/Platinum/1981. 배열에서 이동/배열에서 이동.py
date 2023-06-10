from collections import deque

n = int(input())
board = [[*map(int, input().split())] for _ in range(n)]

# 배열 내부의 가장 작은 값, 큰 값 구하기
min_v, max_v = 200, 0
for i in range(n):
    min_v = min(min_v, min(board[i]))
    max_v = max(max_v, max(board[i]))


# 최대, 최소 값이 범위 내로 n-1, n-1에 도착할 수 있으면 1을 반환 아니라면 0을 반환하는 함수
def bfs(left, right):
    que = deque([(0, 0)])
    v = [[False] * n for _ in range(n)]
    v[0][0] = True

    while que:
        x, y = que.popleft()
        if x == n-1 and y == n-1:
            return True

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not v[nx][ny] and left <= board[nx][ny] <= right:
                v[nx][ny] = True
                que.append((nx, ny))
    return False


def check(mid):
    for i in range(min_v, max_v + 1): # 최대-최소 값이 최소값이 i, 그 차이가 mid일 경우 bfs
        if i <= board[0][0] <= i + mid and i <= board[-1][-1] <= i + mid: # bfs탐색을 덜 할 수 있게하는 조건
            if bfs(i, i + mid):
                return True
    return False

        
start = 0               # 최대, 최소값의 차이를 구할 시작점
end = max_v - min_v     # 최대, 최소값의 차이
while start <= end:     # 분할 정복이 끝남을 의미
    mid = (start + end) // 2    # 분할 정복을 위한 가운데를 의미

    if check(mid):
        end = mid - 1
    else:
        start = mid + 1
print(end + 1)

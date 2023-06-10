from collections import deque

n = int(input())
board = [[*map(int, input().split())] for _ in range(n)]

# 배열 내부의 가장 작은 값, 큰 값 구하기
min_v, max_v = 1e9, 0
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


start = 0               # 이 값이 왜 min_v이면 안됨?
end = max_v - min_v     # 이 값은 무슨 의미를 갖는 거지?
while start <= end:     # 분할 정복이 끝남을 의미
    mid = (start + end) // 2    # 분할 정복을 위한 가운데를 의미

    suc = False
    for i in range(min_v, max_v+1):
        if i <= board[0][0] <= i + mid and i <= board[-1][-1] <= i + mid:   # bfs탐색을 덜 하기 위한 조건
            check = bfs(i, i+mid)
            if check:
                suc = True
                break
    if suc:
        end = mid - 1
    else:
        start = mid + 1
print(end + 1)

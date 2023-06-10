from collections import deque

n = int(input())
board = [[*map(int, input().split())]for _ in range(n)]

min_v, max_v = 1e9, 0
for i in range(n):
    min_v = min(min_v, min(board[i]))
    max_v = max(max_v, max(board[i]))

s, e = board[0][0], board[-1][-1]       # 시작 위치와 도착 위치


def bfs(left, right):
    que = deque([(0, 0)])
    v = [[False] * n for _ in range(n)]
    v[0][0] = True

    while que:
        x, y = que.popleft()
        if x == n-1 and y == n-1:   # 최솟값이 left, 최댓값이 right 범위 내에서 도착 위치까지 도달이 가능함!
            return True
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < n and 0 <= ny < n): continue
            if v[nx][ny]: continue
            if not (left <= board[nx][ny] <= right): continue
            v[nx][ny] = True
            que.append((nx, ny))


def check(mid):
    for i in range(min_v, max_v + 1):   # min_v 부터 max_v까지 가능한 배열에서 등장하는 모든 숫자에 대해서 mid 최대 최소 차이가 나는 경우가 있는 지 구해본다
        if i <= s <= i + mid and i <= e <= i + mid:
            if bfs(i, i+mid):
                return True
    return False


left, right = 0, max_v - min_v          # 이분 탐색으로 최댓값과 최솟값의 차이가 가장 작은 경우를 구한다
                                        # max_v - min_v 는 최댓값과 최솟값의 차이 중 최대
while left <= right:
    mid = (left + right) // 2

    # 최대값, 최소값의 차이가 mid값일 때 시작 위치에서 도착 위치까지 도달이 가능하다면
    if check(mid):
        right = mid - 1
    else:
        left = mid + 1
print(right + 1)

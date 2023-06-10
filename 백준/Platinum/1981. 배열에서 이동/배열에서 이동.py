from collections import deque
import sys
 
input = sys.stdin.readline
N = int(input())
board = []
MIN, MAX = 256, -1
for _ in range(N):
    inputs = list(map(int, input().split()))
    for num in inputs:
        MIN = min(MIN, num)
        MAX = max(MAX, num)
    board.append(inputs)
s, e = board[0][0], board[N - 1][N - 1]
dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
 
 
def check(mid):
    condition = MAX + 1
    for i in range(MIN, condition):
        if not (i <= s <= i + mid and i <= e <= i + mid):
            continue
        if bfs(i, i + mid):
            return True
    return False
 
 
def bfs(a, b):
    visit = [[False for _ in range(N)] for _ in range(N)]
    visit[0][0] = True
    q = deque([(0, 0)])
    while q:
        hereY, hereX = q.popleft()
        if hereY == N - 1 and hereX == N - 1:
            return True
        for d in dir:
            thereY, thereX = hereY + d[0], hereX + d[1]
            # 배열 범위를 벗어나면 패스
            if thereY < 0 or thereY >= N or thereX < 0 or thereX >= N:
                continue
            # 방문했던 곳 패스
            if visit[thereY][thereX]:
                continue
            num = board[thereY][thereX]
            # 값 범위를 벗어나는 곳 패스
            if not (a <= num <= b):
                continue
            visit[thereY][thereX] = True
            q.append((thereY, thereX))
 
 
def main():
    left, right = 0, MAX
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    print(ans)
 
 
if __name__ == '__main__':
    main()
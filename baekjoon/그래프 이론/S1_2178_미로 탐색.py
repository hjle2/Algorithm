def solve():
    que = [(0, 0)]
    while que:
        x, y = que.pop(0)
        if x == N-1 and y == M-1:
            return A[x][y]
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx ,ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and A[nx][ny] == 1:
                que.append((nx, ny))
                A[nx][ny] = A[x][y] + 1
    return A[N-1][M-1]

N, M = map(int, input().split())
A = [[*map(int, [*input()])]for _ in range(N)]
print(solve())
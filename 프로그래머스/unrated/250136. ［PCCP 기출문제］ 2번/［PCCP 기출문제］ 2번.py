from collections import deque

def solution(land):
    n, m = len(land), len(land[0])
    answer = [0] * m
    
    chk = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if land[i][j] and not chk[i][j]:
                que = deque([(i, j)])
                chk[i][j] = True
                cols = set()
                cnt = 0
                while que:
                    x, y = que.popleft()
                    cols.add(y)
                    cnt += 1
                    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m and not chk[nx][ny] and land[nx][ny]:
                            chk[nx][ny] = True
                            que.append((nx, ny))
                for k in cols:
                    answer[k] += cnt
    return max(answer)

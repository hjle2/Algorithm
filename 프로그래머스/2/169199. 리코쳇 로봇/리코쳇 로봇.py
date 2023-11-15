from collections import deque

def solution(board):
    
    n, m = len(board), len(board[0])
    visited = [[False] * m for _ in range(n)]
    board = [list(board[i]) for i in range(n)]
    
    # 로봇의 초기 위치 찾기
    x, y = 0, 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                x, y = i, j
                board[i][j] = '.'
                visited[i][j] = True
                
    que = deque([(x, y, 0)])
    while que:
        x, y, cnt = que.popleft()
        if board[x][y] == 'G':
            return cnt
        
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = get_nxny(x, y, dx, dy, board, n, m)
            if visited[nx][ny]: continue
            if x != nx or y != ny:
                que.append((nx, ny, cnt + 1))
                visited[nx][ny] = True
    return -1


def get_nxny(x, y, dx, dy, board, n, m):
    while 0 <= x < n and 0 <= y < m and board[x][y] != 'D':
        x += dx
        y += dy
    return x - dx, y - dy
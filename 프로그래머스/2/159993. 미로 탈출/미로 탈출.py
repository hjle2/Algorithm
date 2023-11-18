from collections import deque

def solution(maps):
    return get_time(maps)
    
    
def get_start_XY(maps):
    n, m = len(maps), len(maps[0])
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                return i, j
            
            
def get_time(maps):
    ret = 0
    n, m = len(maps), len(maps[0])
    x, y = get_start_XY(maps)   # 시작 좌표
    que = deque([(x, y, 0)])
    visited = [[False] * m for _ in range(n)]
    visited[x][y] = True
    
    flag = False    # 레버까지 도착할 수 있는지 여부
    
    # 레버까지 이동하는데 걸리는 최소 시간 구하기
    while que:
        x, y, t = que.popleft()
        if maps[x][y] == 'L':
            flag = True
            break
        
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != 'X':
                visited[nx][ny] = True
                que.append((nx, ny, t+1))
    
    if not flag:    # 레버까지 도달할 수 없다면 -1 반환
        return -1
    
    ret += t

    que = deque([(x, y, 0)])
    visited = [[False] * m for _ in range(n)]
    visited[x][y] = True
    
    flag = False    # 출구까지 도착할 수 있는지 여부
    
    while que:
        x, y, t = que.popleft()
        if maps[x][y] == 'E':
            flag = True
            break
        
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != 'X':
                visited[nx][ny] = True
                que.append((nx, ny, t+1))
    
    if not flag:    # 출구까지 도달할 수 없다면 -1 반환
        return -1
            
    ret += t
    
    return ret
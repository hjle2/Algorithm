import sys
sys.setrecursionlimit(10**8)
answer = 'z'

def in_range(nx, ny, n, m):
    return 1 <= nx <= n and 1 <= ny <= m


def dfs(n, m, x, y, r, c, s, cnt, k):
    global answer
    if k < cnt + abs(x - r) + abs(y - c):
        return
    if x == r and y == c and cnt == k:
        answer = s
        return
    
    for dx, dy, ch in [(1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r'), (-1, 0, 'u')]:
        nx, ny = x + dx, y + dy
        if in_range(nx, ny, n, m) and s + ch < answer:
            dfs(n, m, nx, ny, r, c, s + ch, cnt + 1, k)
        

def solution(n, m, x, y, r, c, k):
    distance = abs(x - r) + abs(y - c)
    if distance > k or (k - distance) % 2 == 1:
        return "impossible"
    
    dfs(n, m, x, y, r, c, '', 0, k)
    
    return answer
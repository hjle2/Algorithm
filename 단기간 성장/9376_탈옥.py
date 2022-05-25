from collections import deque

# 1. 죄수 1이 죄수 2를 데리고 나가는 경우
# 2. 죄수 2가 죄수 1을 데리고 나가는 경우
# 3. 상근이가 죄수 1, 2를 데리러 가는 경우
# 위 세가지 경우에 각 좌표에 문을 여는 횟수를 계산한다.
# 각 경우의 문을 여는 횟수를 모두 더하고,
# 문의 위치는 중복되여 문이 열린 횟수 2회를 빼준다.
# 세가지 경우가 지나간 좌표 중에서 최소값이 정답이 된다.
# 문이 아닐 경우에는 appendleft를 사용하여 먼저 탐색할 수 있도록 하고,
# 문일 경우에는 append 를 하여 문이 없는 경우보다 나중에 탐색하도록 한다.


def bfs(r, c):
    q = deque([(r, c)])
    dist  = [[-1]*C for _ in range(R)]
    dist[r][c] = 0
    while q:
        r, c = q.popleft()
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if 0<=nr<R and 0<=nc<C and dist[nr][nc] < 0 and A[nr][nc] != '*':
                if A[nr][nc] == '.':
                    dist[nr][nc] = dist[r][c]
                    q.appendleft((nr, nc))
                elif A[nr][nc] == '#':
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
    return dist


def find_prisoner():
    que = deque([(0, 0)])
    for r in range(R):
        for c in range(C):
            if A[r][c] == '$':
                que.append((r, c))
                A[r][c] = '.'
    return que


d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for _ in range(int(input())):
    R, C = map(int, input().split())
    A = [[*input()]for _ in range(R)]
    for r in range(R):
        A[r].insert(0, '.')
        A[r].append('.')
    R, C = R+2, C+2
    A.insert(0, ['.'] * C)
    A.append(['.'] * C)

    que = find_prisoner()
    r, c = que.popleft()
    d1 = bfs(r, c)
    r, c = que.popleft()
    d2 = bfs(r, c)
    r, c = que.popleft()
    d3 = bfs(r, c)

    ans = R * C
    for r in range(R):
        for c in range(C):
            if d1[r][c] >= 0 and d2[r][c] >= 0 and d3[r][c] >= 0:
                k = d1[r][c] + d2[r][c] + d3[r][c]
                if A[r][c] == '#': k -= 2
                ans = min(ans, k)
    print(ans)

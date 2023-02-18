# 각 칸에 램프가 들어있는 직사각형 모양의 탁자
# 램프는 켜져 있거나 꺼져있다
# 열의 아래에 스위치가 있고, 스위치를 누를때마다 상태가 반대로 바뀐다
# 어떤 행의 모든 램프가 켜져 있을 때 그 행이 켜져있다 말한다
# 스위치를 K 번 눌러 켜져있는 행의 최대값을 구하라

import sys
input = sys.stdin.readline

def solve():
    ret = 0
    for i in range(N):
        if visited[i]: continue
        visited[i] = 1
        cnt = 0
        for c in A[i]:
            if c == '0':
                cnt += 1
        if cnt > K or (K-cnt)%2 != 0:
            continue
        ans = 1
        for j in range(i+1, N):
            if A[i] == A[j]:
                ans += 1
        ret = max(ans, ret)
    return ret

N, M = map(int, input().split())
A = [input()for _ in range(N)]
visited = [0] * N
K = int(input())
print(solve())
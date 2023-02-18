# 예선에 총 n개의 팀 (작년과 동일한 팀) 참가
# 올해는 최종 순위를 발표하지 않는다
# 하지만, 작년에 비해 순위가 바뀐 팀의 목록만 발표한다 (작년엔 발표함)
# 올해 a팀이 b팀보다 높았는데 올해 b팀이 a팀보다 높다면, (b, a)를 발표할 것이다
# 이 정보를 갖고 올해 최종 순위를 만들어보고자 한다
# 확실하지 않을 수도 있고, 잘못된 정보일 수 있다..
# 순위를 알아낼 수 없는 경우는 IMPOSSIBLE을 출력
import sys
from collections import deque

input = sys.stdin.readline
INF = 1e9
def main():
    N = int(input()) + 1
    # 작년에 i등을 한 팀의 번호, 모든 Ti 는 다르다
    T = [0, *map(int, input().split())]
    rel = [[]for _ in range(N)]
    cnt = [0] * N
    for i in range(1, N):
        for j in range(i+1, N):
            rel[T[i]].append(T[j])
            cnt[T[j]] += 1
    M = int(input())
    for _ in range(M):
        a, b = map(int, input().split())
        if a in rel[b]:
            rel[b].remove(a)
            cnt[a] -= 1
        elif b in rel[a]:
            rel[a].remove(b)
            cnt[b] -= 1
        rel[a].append(b)
        cnt[b] += 1
    que = deque()
    for i in range(1, N):
        if not cnt[i]:
            que.append(i)
    while que:
        x = que.popleft()
        print(x, end=' ')
        for nxt in rel[x]:
            cnt[nxt] -= 1
            if cnt[nxt] == 0:
                que.append(nxt)
    print()



for _ in range(int(input())):
    main()
# in:
# 1
# 5
# 1 5 2 3 4
# 2
# 2 4
# 3 4
#
# answer:
# 1 5 4 2 3
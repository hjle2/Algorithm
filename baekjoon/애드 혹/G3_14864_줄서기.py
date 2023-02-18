# N 명의 학생이 앞뒤로 일렬로 서 있고, 서로 다른 번호가 적힌 카드를 하나 갖고 있다
# 자신보다 뒤에 서 있으면서 더 작은 번호의 카드를 가진 학생들의 명단을 받았다
# 이 명단을 통해 학생들이 갖고 있는 카드 번호를 알아내려고 한다
# 명단은 순서쌍으로 만들어져 있다
# (X, Y) 는 Y 학생이 X 학생보다 뒤에 서있고, 더 작은 번호를 갖고 있다는 의미이다
# 명단으로 학생들의 카드 번호를 알 수 있으면 순서대로 출력 아니라면 -1 출력해라
def printAns():
    cnt = [0] * (N+1)
    for i in range(1, N+1):
        if cnt[v[i]]:
            print(-1)
            return
        cnt[v[i]] += 1
    print(*v[1:], sep=' ')

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
v = [i for i in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    v[a] += 1
    v[b] -= 1
    if v[b] < 1 or v[a] > N:
        print(-1)
        exit()
printAns()
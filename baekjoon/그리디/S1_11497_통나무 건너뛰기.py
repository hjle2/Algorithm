# N 개의 통나무를 원형으로 세워놓고 뛰어노려고 한다
# 인접한 통나무의 높이 차가 최소가 되게 하려 한다
# 건너뛰기의 난이도는 인접한 두 통나무 간의 높이 차의 최댓값으로 결정된다
# 첫번째와 마지막의 통나무 또한 인접해 있다

import sys
input = sys.stdin.readline
def getLevel():
    ret = 0
    for i in range(2, N):
        ret = max(ret, L[i]-L[i-1], L[i]-L[i-2])
    return ret

for _ in range(int(input())):
    N = int(input())
    L = [*map(int, input().split())]
    L.sort()
    print(getLevel())
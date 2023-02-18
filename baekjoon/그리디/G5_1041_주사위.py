# 주사위의 전개도가 있다
# 수가 바깥으로 하여 접는다
# 각 알파벳에 수가 쓰여 있다
# 지민이는 동일한 주사위를 N^3개 갖고 있다
# 이 주사위를 적절히 회전시키고, 쌓아 N*N*N크기의 정육면체를 만드려고 한다
# 이 정육면체은 탁자위에 있으므로 5개의 면이 보인다
# 5개의 면에 쓰인 수의 합의 최솟값을 출력하는 프로그램을 작성하라
# 0 1 2
# 0 1 3
# 0 2 4
# 0
from copy import deepcopy
def getMin3surf():
    minv = 10**6*3
    ret = []
    for i in range(6):
        for j in range(6):
            if j == i or j == 5-i or D[i] + D[j] > minv:
                continue
            for k in range(6):
                if k == i or k == j or k == 5-i or k == 5-j:
                    continue
                if minv > D[i] + D[j] + D[k]:
                    minv = D[i] + D[j] + D[k]
                    ret = [D[i], D[j], D[k]]
    return sorted(ret)

def getAns():
    tmp = getMin3surf()
    if N > 1:
        return tmp[2] * 4 + tmp[1] * (N-1) * 8 + tmp[0] * (N*N + (N-1)*(N-1)*4)
    else:
        return sum(D) - max(D)


N = int(input())
D = [*map(int, input().split())]
print(getAns())


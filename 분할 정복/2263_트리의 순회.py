# 프리오더
# 탑 (탑 = 왼) (탑 = 오)
# 인오더
# (탑 = 왼) 탑 (탑 = 오)
# 포스트오더
# (탑 = 왼) (탑 = 오) 탑
# 왼쪽 아래부터 가장 낮은 노트부터 탐색

# 7
# 4 2 6 5 1 3 7
# 4 6 5 2 7 3 1
#
# 1 2 4 5 6 3 7
#
# 8
# 5 3 6 2 7 4 8 1
# 5 6 3 7 8 4 2 1
#
# 1 2 3 5 6 4 7 8
#
# 8
# 1 5 3 6 2 7 4 8
# 5 6 3 7 8 4 2 1
#
# 1 2 3 5 6 4 7 8
import sys

sys.setrecursionlimit(10**6)
def getPreorder(inL, inR, postL, postR):
    if inL > inR or postL > postR:
        return
    root = postorder[postR]
    print(root, end=' ')

    getPreorder(inL, idx[root]-1, postL, postL + idx[root] - inL - 1)
    getPreorder(idx[root]+1, inR, postL + idx[root] - inL, postR-1)


N = int(input())
inorder = [*map(int, input().split())]
postorder = [*map(int, input().split())]
idx = [0] * (N+1)
for i in range(N):
    idx[inorder[i]] = i
getPreorder(0, N-1, 0, N-1)
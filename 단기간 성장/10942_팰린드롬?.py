# 홍준이가 적은 N개의 자연수
# 명우에게 질문 M번
import sys

input = sys.stdin.readline

dp = []
nums = []
def getDPVal(i, j):
    if i == 0: return 1
    if nums[j] != nums[j+i]:
        return 0

    for k in range(1, i//2+1):
        i-=2;j+=1
        if i%2 and not dp[i][j]:
            return 0
    return 1

def makeDP(N, nums, M):
    global dp
    dp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N-i):
            dp[i][j] = getDPVal(i, j)


def solve():
    global nums
    N = int(input())
    nums = [*map(int, input().split())]
    M = int(input())
    makeDP(N, nums, M)

    for i in range(M):
        s, e = map(int, input().split())
        print(dp[e-s][s-1])


if __name__ == "__main__":
    solve()


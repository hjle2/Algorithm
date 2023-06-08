import sys
input = sys.stdin.readline
# s부터 e까지의 수가 팰린드롬이면, 1 아니라면, 0을 반환하는 함수
# def is_palindrome(s, e):
#     # s == e 라면 1자리 숫자 일 때 이므로!
#     if s == e:
#         return 1
#
#     if arr[s-1] != arr[e-1]:
#         return 0
#     if s + 1 == e and arr[s-1] == arr[e-1]:
#         return 1
#     return is_palindrome(s+1, e-1)

def get_dp_val(i, j):
    # 숫자가 1개일 때는 무조건 팰린드롬임
    if i == 0: return 1
    # 시작 숫자와 끝 숫자가 다르면 팰린드롬이 아님
    if arr[i+j] != arr[j]:
        return 0
    # 시작 숫자와 끝 숫자가 같고, 숫자가 2개라면 팰린드롬임
    if i == 1:
        return 1
    # 다음 팰린드롬은 시작, 끝을 제거 (길이가 2줄어 들어 i-2), 시작 인덱스는 + 1 (j+1)
    return dp[i-2][j+1]


def make_dp():
    global dp
    # i부터 j개의 숫자가 팰린드롬인지의 여부
    dp = [[0] * n for _ in range(n)]
    # 팰린드롬의 개수
    for i in range(n):
        # 시작 인덱스
        for j in range(n-i):
            dp[i][j] = get_dp_val(i, j)


# 수열의 크기 n
n = int(input())
# 수열 arr
arr = [*map(int, input().split())]

# 홍준이가 한 질문의 개수
m = int(input())
# 홍준이의 질문 s, e
se = [[*map(int, input().split())]for _ in range(m)]
make_dp()

for i in range(m):
    s, e = se[i]
    print(dp[e-s][s-1])
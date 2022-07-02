# N = int(input())
# # A 는 오름차순, B 는 내림차순
# # A[0] = 1, B[N-1] = 0
# A = [*map(int, input().split())]
# B = [*map(int, input().split())]
#
# # dp[i] 는 i번째의 나무를 0까지 자르는데 필요한 최소의 비용
# dp = [0] * N
# for i in range(1, N):
#     dp[i] = min(dp[j] + A[i] * B[j] for j in range(i))
# print(dp[-1])

# 블록 껍질 최적화 Convex Hull Trick
# 특이한 모양의 DP 점화식을 빠르게 계산
# 배열 B 의 값이 항상 감소한다는 조건에 주목하여
# 배열 B 의 값을 x값으로, dp 의 값을 y값으로 계산하여
# k에 x 축 기준으로 낮은 값만 저장한다 즉, B[i]를 사용하였을 때의 최솟 값

# f, g 의  [1] 은 dp 값, [0] 은 비용
# 그래프 상으로 표현 한다면.. 기울기
# f 가 더 높은 x B[x] 를 갖고 있기 때문에
# 원래라면 g[1]-f[1] // g[0]-f[0]이여야 하지만
# g[0] - f[0] 을 반대로 f[0] - g[0] 으로 해주었음
def getX(f, g):
    return (g[1] - f[1])//(f[0] - g[0])


def insert(x):
    k.append(x)
    # 추가된 x 의 기울기가 더 높으면, 제거 한다
    # 기울기가 낮음 -> 같은 x 값에 대하여 더 낮은 y값을 갖는다.
    while len(k) > 2 and getX(k[-3], k[-2]) > getX(k[-2], k[-1]):
        k.pop(-2)


# x 는 현재 나무의 높이
# x 나무 높이를 0까지 자르는 데의 최소 비용을 구하는 함수
def bs(x):
    l, r = 0, len(k) - 1
    while l < r:
        mid = (l+r)//2
        # getX 는 기울기 아닌가..
        # 기울기를 높이랑 왜 비교하지..?
        print(getX(k[mid], k[mid+1]), x)
        if getX(k[mid], k[mid+1]) <= x:
            l = mid+1
        else:
            r = mid
    # k[l][0] 은 B[0]으로 비용
    # x 는 현재 나무의 높이
    # k[l][1] 은 dp[l]
    return k[l][0] * x + k[l][1]


N = int(input())
A = [*map(int, input().split())]
B = [*map(int, input().split())]
dp = [0] * N
k = [(B[0], 0)]
for i in range(1, N):
    dp[i] = bs(A[i])
    insert((B[i], dp[i]))
print(dp[-1])

# CHT Convex Hull Trick 블록 껍질 최적화 방법
# 최소 값만을 구할 때, 2차 평면에서 증가하는 x에 대해서 최소 y를 갖는 방식으로 푼다.
def getdp(i):
    print()



N = int(input())
# 나무의 높이
A = [*map(int, input().split())]
# 비용
# 계산하는데 계속 필요하므로 X축
B = [*map(int, input().split())]
# 해당 인덱스의 나무를 자르는데에 필요한 최소 비용
# "최소" 비용을 저장하므로 Y축
dp = [0] * N

for i in range(1, N):
    dp[i] = getdp(i)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ar = [*map(int, input().split())]
sum = 0
# sum[i] % M == sum[j] % M 인 i, j의 갯수를 찾아라
cnt = [0] * M
# 각 나머지가 index 인 구간의 갯수
for i in range(N):
    sum += ar[i]
    sum %= M
    cnt[sum] += 1

ans = cnt[0]
# 0 부터 시작하는 구간 중에 나머지가 0인 구간 포함!
# nC2 = n ! // 2 // (n-2) -> n * n-1 / 2
for i in range(M):
    ans += cnt[i] * (cnt[i]-1) // 2
print(ans)
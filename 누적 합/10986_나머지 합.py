import sys

input = sys.stdin.readline
N, M = map(int, input().split())
ar = [*map(int, input().split())]
# 와 사람들 천재 많다....
# 배열의 구간 연속 합은 sum[j] - sum[i]
# 이 문제는 연속 합의 나머지가 0인 i, j 쌍의 갯수를 구해야 한다
# 여기에서 (sum[j] - sum[i]) % M == 0 인 i, j쌍은
# sum[j] % M - sum[i] % M == 0
# sum[j] % M == sum[i] % M 인 i, j 쌍의 갯수를 구해야 한다. !! 이 부분이 포인트

sum = 0
cnt = [0] * M
for i in range(N):
    sum += ar[i]
    sum %= M
    cnt[sum] += 1

ans = cnt[0]
for i in range(M):
    # cnt[i] = sum[i]%M 이 v인 i 의 갯수 n
    # 이 중에 두개를 뽑아 i, j 쌍을 만드는 경우의 수를 구한다!
    ans += cnt[i] * (cnt[i]-1) // 2

print(ans)

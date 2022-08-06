# 학교에서 측정한 온도가 어떤 정수의 수열
# 연속적인 며칠 동안 온도의 합이 가장 큰 값

N, K = map(int, input().split())
ar = [*map(int, input().split())]
sum = [ar[0]]
for i in range(1, N):
    sum.append(sum[i-1] + ar[i])

print(max(sum[i] - sum[i-K] for i in range(K, N)))
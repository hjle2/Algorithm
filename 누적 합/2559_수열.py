# 학교에서 측정한 온도가 어떤 정수의 수열
# 연속적인 며칠 동안 온도의 합이 가장 큰 값

N, K = map(int, input().split())
ar = [0, *map(int, input().split())]
for i in range(1, N+1):
    ar[i] += ar[i-1]

print(max(ar[i] - ar[i-K] for i in range(K, N+1)))
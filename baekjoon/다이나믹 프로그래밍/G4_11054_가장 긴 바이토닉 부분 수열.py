N = int(input())
A = [*map(int, input().split())]
updp = [1] * N
downdp = [1] * N
for i in range(1, N):
    for j in range(i-1, -1, -1):
        if A[i] > A[j]:
            updp[i] = max(updp[i], updp[j]+1)
for i in range(N-2, -1, -1):
    for j in range(i+1, N):
        if A[i] > A[j]:
            downdp[i] = max(downdp[i], downdp[j]+1)
print(max(updp[i] + downdp[i] - 1for i in range(N)))

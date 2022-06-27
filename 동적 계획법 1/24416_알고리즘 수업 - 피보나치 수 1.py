N = int(input())
f = [0] * N
f[0] = f[1] = 1
for i in range(2, N):
    f[i] = f[i-1] + f[i-2]
print(f[-1], N-2)

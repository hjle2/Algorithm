N = int(input())
f0, f1 = 0, 1
for i in range(2, N+1):
    f0, f1 = f1, f0 + f1
print(f1)
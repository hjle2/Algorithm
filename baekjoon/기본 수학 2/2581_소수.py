import math
def printAns():
    ans1, ans2 = 0, 1e9
    for i in range(N, M+1):
        if ar[i]:
            ans1 += i
            ans2 = min(ans2, i)
    print(ans1, ans2, sep='\n') if ans2 < 1e9 else print(-1)


N, M = int(input()), int(input())
ar = [1] * (M+1)
ar[0] = ar[1] = 0
for i in range(2, int(math.sqrt(M))+1):
    for j in range(max(i+1, N), M+1):
        if ar[j] and j%i == 0:
            ar[j] = 0
printAns()
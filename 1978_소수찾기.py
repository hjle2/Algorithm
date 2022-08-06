import math

N = int(input())
ar = [*map(int, input().split())]
l = max(ar)
od = [0] * (l + 1)
od[0] = 0
for i in ar:
    if i > 1:
        od[i] += 1

for i in range(2, int(math.sqrt(l))+1):
    for j in range(i+1, len(od)):
        if od[j] and j % i == 0:
            od[j] = 0
print(sum(od))

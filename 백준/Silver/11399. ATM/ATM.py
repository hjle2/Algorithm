n = int(input())
p = sorted([*map(int, input().split())])

# 걍 순서대로 시간이 족므 걸리는 순서대로 뽑아야 하는 거 아니야,,?
sum = 0
t = 0
for pi in p:
    sum += pi + t
    t += pi

print(sum)
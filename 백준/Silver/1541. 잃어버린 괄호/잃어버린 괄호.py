import sys
si = sys.stdin.readline

exp = []
for i in input().split('-'):
    tmp = 0
    for j in i.split('+'):
        tmp += int(j)
    exp.append(tmp)
print(exp.pop(0) - sum(exp))

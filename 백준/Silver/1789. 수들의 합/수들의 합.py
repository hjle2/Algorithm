import sys
input = sys.stdin.readline

n = int(input())
hap = 0
i = 1
while hap + i <= n:
    hap += i
    i += 1
print(i-1)
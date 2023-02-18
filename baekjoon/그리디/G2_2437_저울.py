import sys
input = sys.stdin.readline
N = int(input())
A = [*map(int, input().split())]
A.sort()
s = 0
for n in A:
    if s+1 < n:
        print(s+1)
        exit()
        break
    s += n
print(s+1)
# i 까지의 합 sum 은 sum 까지의 무게는 측정 가능하다는 의미
# 다음 추가 s+1 보다 더 크다면 s+1 에 해당되는 수는 만들 수 없다는 의미

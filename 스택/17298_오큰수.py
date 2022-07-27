import sys

input = sys.stdin.readline
N = int(input())
ar = [*map(int, input().split())]

# 감소하고 있으면 stack에 담는다!
# 처음으로 증가하는 수를 만나면 해당 값으로 더 작은 값들 초기화
# 해당 값의 인덱스도 stack에 담아서 이어서
# 더 큰 수를 만나지 못해서 stack에서 나오지 못한 수는 모두 -1
stack = []
for i in range(N):
    if not stack:
        stack.append(i)
        continue
    if ar[stack[-1]] >= ar[i]:
        stack.append(i)
    else:
        while stack and ar[stack[-1]] < ar[i]:
            ar[stack.pop()] = ar[i]
        stack.append(i)
for i in stack:
    ar[i] = -1
print(*ar, sep=' ')
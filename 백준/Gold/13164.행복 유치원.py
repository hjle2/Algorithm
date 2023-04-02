n, k = map(int, input().split())
nums = sorted([*map(int, input().split())])
sub = []
for i in range(n-1):
    sub.append(nums[i+1] - nums[i])
sub.sort()
for i in range(k-1):
    sub.pop()
print(sum(sub))

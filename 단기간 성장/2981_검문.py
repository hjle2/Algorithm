def GCD(a, b):
    if a%b == 0:
        return b
    else:
        return GCD(b, a%b)


N = int(input())
nums = [int(input())for _ in range(N)]
nums.sort()
gcd = nums[1] - nums[0]

for i in range(1, N-1):
    gcd = GCD(gcd, nums[i+1] - nums[i])

lst = []
for i in range(1, gcd+1):
    if gcd % i == 0:
        if gcd // i not in lst:
            lst.append(gcd//i)
        if i not in lst:
            lst.append(i)
lst.remove(1)
lst.sort()
for i in lst:
    print(i, end=' ')
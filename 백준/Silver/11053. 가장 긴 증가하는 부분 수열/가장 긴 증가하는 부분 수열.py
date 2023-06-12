n = int(input())
ar = [*map(int, input().split())]

LIS = [0]
for num in ar:
    if LIS[-1] < num:
        LIS.append(num)
    else:
        l, r = 1, len(LIS) - 1
        while l <= r:
            m = (l + r) // 2
            if LIS[m] < num:
                l = m + 1
            else:
                r = m - 1
        LIS[r+1] = num
print(len(LIS)-1)
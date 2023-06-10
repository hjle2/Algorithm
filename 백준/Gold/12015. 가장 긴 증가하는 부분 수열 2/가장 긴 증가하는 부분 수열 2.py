n = int(input())
arr = [*map(int, input().split())]

LIS = [0]

for num in arr:
    if LIS[-1] < num:
        LIS.append(num)
    else:
        left = 0
        right = len(LIS) - 1

        while left < right:
            mid = (left + right) // 2
            if LIS[mid] < num:
                left = mid + 1
            else:
                right = mid
        LIS[right] = num
print(len(LIS) - 1)
n = int(input())
arr = [*map(int, input().split())]

LIS = [0]

for num in arr:
    if LIS[-1] < num:
        LIS.append(num)
    else:   # 증가하는 숫자가 아니라면, 현재 숫자가 들어갈 위치를 이분 탐색으로 찾는다.
        left = 0
        right = len(LIS) - 1

        while left <= right:
            mid = (left + right) // 2
            if LIS[mid] < num:
                left = mid + 1
            else:
                right = mid-1 # mid + 1 이 아닌 mid 값을 할당하기 때문에 while문의 조건에 등호가 빠져야 한다.
        LIS[right+1] = num
print(len(LIS) - 1)

# 1~N
def solution_timeout(food_times, k):
    n = len(food_times)
    cnt = 0
    i = 0
    for _ in range(k):
        food_times[i] -= 1
        if food_times[i] == 0:
            cnt += 1
            if cnt == n:
                return -1
        while True:
            i = (i+1)%n
            if food_times[i]: break
    return i+1


solution([3, 1, 2], 5)
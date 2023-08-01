def solution(temperature, t1, t2, a, b, onboard):
    # add 10
    temperature += 10
    t1 += 10
    t2 += 10
    
    min_t, max_t = min(temperature, t1), max(temperature, t2)
    n = len(onboard)
    dp = [[10 ** 9] * (max_t + 1) for _ in range(n)]
    
    dp[0][temperature] = 0
    start, end = min_t, max_t
    for i in range(1, n):
        if onboard[i]:
            start, end = t1, t2
        else:
            start, end = min_t, max_t
            
        for j in range(start, end+1):
            if j < temperature:     # 가만히 있으면 온도가 올라감
                tmp = dp[i-1][j] + b
                if j-1 >= 0:
                    tmp = min(tmp, dp[i-1][j-1])
                if j+1 <= max_t:
                    tmp = min(tmp, dp[i-1][j+1] + a)
                
            elif j > temperature:   # 가만히 있으면 온도가 내려감
                tmp = dp[i-1][j] + b
                if j-1 >= 0:
                    tmp = min(tmp, dp[i-1][j-1] + a)
                if j+1 <= max_t:
                    tmp = min(tmp, dp[i-1][j+1])
            else:
                tmp = dp[i-1][j]
                if j-1 >= 0:
                    tmp = min(tmp, dp[i-1][j-1])
                if j+1 <= max_t:
                    tmp = min(tmp, dp[i-1][j+1])
                
            dp[i][j] = tmp
            
#     for i in range(n):
#         print(dp[i])
            

    return min(dp[-1])
# 다이나믹 프로그래밍으로 풀어야 하는 문제
def solution(temperature, t1, t2, a, b, onboard):
    temperature += 10
    t1 += 10
    t2 += 10
    
    min_t, max_t = min(t1, temperature), max(t2, temperature)
    n = len(onboard)
    
    # dp[i][j]는 i분에 j온도를 유지하는 최소 전력의 값
    # 10 ** 5 는 최대 전력을 의미
    dp = [[10 ** 5] * (max_t + 1) for _ in range(n)]
    dp[0][temperature] = 0
    
    # 시간(분)
    for m in range(1, n):
        if onboard[m]:  # 승객이 있으면,
            start, end = t1, t2
        else:           # 승객이 없으면,
            start, end = min_t, max_t
            
        for t in range(start, end+1):
            if t < temperature:     # 실외온도보다 낮음 -> 올라가려는 성질
                tmp = dp[m-1][t] + b    # m-1분에 t(같은 온도)에서 에어컨 동작시켜 b전력 소비
                if t-1 >= 0:        # 실외온도가 더 높기 때문에 전력 소비 X
                    tmp = min(tmp, dp[m-1][t-1])
                if t+1 <= max_t:    # 실외온도가 더 높기 때문에 전력 소비 O
                    tmp = min(tmp, dp[m-1][t+1] + a)
            elif t > temperature:   # 실외온도보다 높음 -> 내려가려는 성질
                tmp = dp[m-1][t] + b
                if t-1 >= 0:
                    tmp = min(tmp, dp[m-1][t-1] + a)
                if t+1 <= max_t:
                    tmp = min(tmp, dp[m-1][t+1])
            else:
                tmp = dp[m-1][t]
                if t-1 >= 0:
                    tmp = min(tmp, dp[m-1][t-1])    # 실외온도 보다 -1이기 때문에 전력 소비 X
                if t+1 <= max_t:
                    tmp = min(tmp, dp[m-1][t+1])    # 실외온도 보다 +1이기 때문에 전력 소비 X
                    
            dp[m][t] = tmp
    
    return min(dp[-1])
import heapq
# 상담유형 k개, 멘토 n명, 상담 요청 [a, b, c] c번 유형의 상담을 원하는 참가자가 a분에 b분동안 상담 요청
# 멘토 인원을 적절히 배정하여 참가자들이 상담을 받기까지 기다린 시간을 모두 합한 최솟값을 return
def solution(k, n, reqs):
    mentos = [1] * k    # 각 유형별로 최소 1명의 멘토가 있어야 한다
    for i in range(n-k):
        idx, val = -1, 1e9   # 멘토가 추가되었을 때 가장 시간을 많이 단축할 수 있는 상담 유형의 인덱스, 단축값
        for i in range(k):
            mentos[i] += 1  # i유형 상담에 멘토 추가!
            tmp = calc_waiting(k, n, reqs, mentos)  # 멘토가 추가되었을때 총 대기 시간
            if tmp < val:
                idx, val = i, tmp
            mentos[i] -= 1
        mentos[idx] += 1
    return calc_waiting(k, n, reqs, mentos)

        
# 멘토들이 mentos배열처럼 배정된 경우에 걸리는 총 대기 시간을 구하는 함수
def calc_waiting(k, n, reqs, mentos):
    end_time = [[]for _ in range(k)]
    for i in range(k):
        for j in range(mentos[i]):  # 배정된 멘토 수 만큼 i유형의 상담을 0에 시작할 수 있다
            end_time[i].append(0)
    
    ret = 0
    for a, b, c in reqs:
        start_time = heapq.heappop(end_time[c-1])       # c 유형 상담을 시작할 수 있는 시간
        start_time = max(start_time, a)                 # 상담이 시작되는 시간
        ret += start_time - a                           # 상담을 받기까지 기다린 시간 계산
        heapq.heappush(end_time[c-1], start_time + b)   # 상담이 끝나는 시간을 다시 heapq에 추가
    return ret
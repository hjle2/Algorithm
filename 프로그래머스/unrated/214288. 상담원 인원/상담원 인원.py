import heapq

def solution(K, N, REQS):
    global k, n, reqs
    k, n, reqs = K, N, REQS
    answer = 0
    mentos = [1] * k
    # 1 ~ k 중에서 가장 많이 추가되어 가장 많이 시간을 단축할 수 있는 멘토를 추가
    for _ in range(n-k):
        org_time = calc(mentos)
        idx, val = 0, 1e9
        for i in range(k):
            mentos[i] += 1
            tmp = calc(mentos)
            if tmp < val:
                idx, val = i, tmp
            mentos[i] -= 1
        mentos[idx] += 1
    return calc(mentos)


def calc(mentos):
    end_time = [[]for _ in range(k)]
    for i in range(k):
        for j in range(mentos[i]):
            end_time[i].append(0)
    
    ret = 0
    for a, b, c in reqs:
        tmp = heapq.heappop(end_time[c-1])
        ret += max(tmp, a) - a
        heapq.heappush(end_time[c-1], max(tmp, a) + b)
    return ret
# 임의의 사원보다 두 점수가 모두 낮은 경우 인센티브를 받지 못한다


def solution(scores):
    wanho = scores.pop(0)
    wanho_t = sum(wanho)
    
    scores.sort(key=lambda x:(-x[0], x[1])) # 근무 태도 기준으로 정렬
    threshold = 0                           # 동료 평가가 이전 동료평가보다 작다면, 둘다 작음을 의미
    rank = 1
    for s1, s2 in scores:
        if s1 > wanho[0] and s2 > wanho[1]: # 원호가 인센티브를 받지 못하는 경우
            return -1
        
        if threshold <= s2:                  # 이전 동료 평가값 max보다 작다면 인센티브를 받지 않는 사람이므로 석차 계산에서 제외한다
            threshold = s2
            if s1 + s2 > wanho_t:
                rank += 1
    return rank
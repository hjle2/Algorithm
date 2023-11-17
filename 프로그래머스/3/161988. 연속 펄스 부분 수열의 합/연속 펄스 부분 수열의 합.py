def solution(sequence):
    answer = -1e9
    n = len(sequence)
    s1 = s2 = 0
    s1_min = s2_min = 0
    pulse = 1
    
    for s in sequence:
        s1 += s * pulse
        s2 -= s * pulse
        
        answer = max(answer, s1-s1_min, s2-s2_min)
        
        s1_min = min(s1_min, s1)
        s2_min = min(s2_min, s2)
        
        pulse *= -1
        
    return answer
def solution(picks, minerals):
    answer = 0
    n = min(sum(picks) * 5, len(minerals))
    cnt_mineral = [[0, 0, 0] for _ in range((n-1) // 5 + 1)]
    
    for i in range(n):
        mineral = minerals[i]
        if mineral == "diamond":
            cnt_mineral[i//5][0] += 1
        elif mineral == "iron":
            cnt_mineral[i//5][1] += 1
        else:
            cnt_mineral[i//5][2] += 1
    
    cnt_mineral.sort(key=lambda x:(-x[0], -x[1], -x[2]))
    
    for d, i, s in cnt_mineral:
        if picks[0]:
            picks[0] -= 1
            answer += d * 1 + i * 1 + s * 1
        elif picks[1]:
            picks[1] -= 1
            answer += d * 5 + i * 1 + s * 1
        elif picks[2]:
            picks[2] -= 1
            answer += d * 25 + i * 5 + s * 1
    return answer
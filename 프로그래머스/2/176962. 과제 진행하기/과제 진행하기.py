def solution(plans):
    answer = []
    pauses = []     # name, 
    cur = [0, 0, 0]    # name, start, playtime
    
    plans.sort(key=lambda x:x[1])
    i = 0
    while i < len(plans):
        name, start, playtime = plans[i]
        tmp = start.split(':')
        start = int(tmp[0]) * 60 + int(tmp[1])
        playtime = int(playtime)
        
        tmp = cur[1] + cur[2]
        
        # print(name, start, playtime)
        # print(tmp)
        
        if tmp == start:
            answer.append(cur[0])
            cur = [name, start, playtime]
            
        elif tmp < start:
            answer.append(cur[0])
            if not pauses:
                cur = [name, start, playtime]
            else:
                pause = pauses.pop()
                cur = [pause[0], tmp, pause[2]]
                i -= 1
                print(pause)
        else:
            pauses.append((cur[0], start, tmp - start))
            cur = [name, start, playtime]
        i += 1
    
    answer.append(cur[0])
    for name, stop, playtime in pauses[::-1]:
        answer.append(name)
    return answer[1:]
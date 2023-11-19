import heapq

# 필요한 최소 객실의 수를 return
def solution(book_time):
    book_time.sort()
    
    answer = 0
    que = []
    for s_t, e_t in book_time:
        s_t, e_t = t2n(s_t), t2n(e_t)
        
        if que:
            earlest_end = heapq.heappop(que)
            if earlest_end > s_t:
                answer += 1
                heapq.heappush(que, earlest_end)
        else:
            answer += 1
        heapq.heappush(que, e_t + 10)
    return answer


def t2n(time):
    time = time.split(':')
    time = int(time[0]) * 60 + int(time[1])
    return time
def solution(sequence, k):
    answer = []
    n = len(sequence)
    
    l, r = 0, 0
    sum = sequence[0]
    
    while l <= r < n:
        if sum == k:
            answer.append((r-l, [l, r]))
        
        if sum < k:
            r += 1
            if r == n:
                break
            sum += sequence[r]
        else:
            sum -= sequence[l]
            l += 1
            if l == n:
                break
        
            
        # print(sum, answer)
    answer.sort()
    return answer[0][1]
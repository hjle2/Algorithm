def solution(m, n, startX, startY, balls):
    answer = []
    
    for x, y in balls:
        dists = []
        
        # 위쪽 벽
        if not (x == startX and y > startY):
            d2 = (x - startX) ** 2 + (y - 2 * n + startY) ** 2
            dists.append(d2)
    
        # 아래쪽 벽
        if not (x == startX and y < startY):
            d2 = (x - startX) ** 2 + (y + startY) ** 2
            dists.append(d2)
        
        # 왼쪽 벽
        if not (y == startY and x < startX):
            d2 = (x + startX) ** 2 + (y - startY) ** 2
            dists.append(d2)
        
        # 오른쪽 벽
        if not (y == startY and x > startX):
            d2 = (x - 2 * m + startX) ** 2 + (y - startY) ** 2
            dists.append(d2)
        
        answer.append(min(dists))
    return answer
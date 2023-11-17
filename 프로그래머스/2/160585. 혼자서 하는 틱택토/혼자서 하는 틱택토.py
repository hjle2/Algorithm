def solution(board):
    cnt_O, cnt_X = get_cnt(board)
    if not (cnt_O == cnt_X or cnt_O == cnt_X+1):
        return 0
    
    flag_O, flag_X = is_done(board, 'O'), is_done(board, 'X')
    
    if flag_O and flag_X:
        return 0
    if flag_O and cnt_O == cnt_X + 1:
        return 1
    if flag_X and cnt_O == cnt_X:
        return 1
    if not flag_O and not flag_X:
        return 1
    return 0

def get_cnt(board):
    n = 3
    cnt_O, cnt_X = 0, 0
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'O':
                cnt_O += 1
            elif board[i][j] == 'X':
                cnt_X += 1
    return cnt_O, cnt_X


def is_done(board, c):
    n = 3
    for i in range(n):
        flag = True
        for j in range(0, n):
            if board[i][j] != c:
                flag = False
                break
        if flag:
            return True
        
        flag = True
        for j in range(0, n):
            if board[j][i] != c:
                flag = False
                break
        if flag:
            return True
        
    flag = True
    for i in range(n):
        if board[i][i] != c:
            flag = False
            break
    
    if flag:
        return True
    
    flag = True
    for i in range(n):
        if board[i][n-1-i] != c:
            flag = False
            break
    
    if flag:
        return True
    
    return False

                
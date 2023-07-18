board = [*input()]

def solve():
    prv = 0
    cnt = 0
    ans = ''
    for i, v in enumerate(board):
        if prv == v:
            cnt += 1
        else:
            if prv == 'X' and cnt % 2:
                return -1
            if prv == 'X':
                if cnt % 4 == 0:
                    ans += 'A' * cnt
                else:
                    ans += 'A' * (cnt - 2) + 'BB'
            prv = v
            cnt = 1
        if v == '.':
            ans += '.'

        if i == len(board)-1:
            if prv =='X' and cnt % 2:
                return -1
            if prv == 'X':
                if cnt % 4 == 0:
                    ans += 'A' * cnt
                else:
                    ans += 'A' * (cnt - 2) + 'BB'
    return ans
print(solve())
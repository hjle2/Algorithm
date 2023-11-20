def update(r, c, v):
    old_s = state[r][c]
    for r in range(N):
        for c in range(N):
            if state[r][c] == old_s:
                table[r][c] = v

def replace(v1, v2):
    for r in range(N):
        for c in range(N):
            if table[r][c] == v1:
                table[r][c] = v2

def merge(r1, c1, r2, c2):
    if table[r1][c1] != 'EMPTY':
        new_v = table[r1][c1]
    else:
        new_v = table[r2][c2]
        
    old_s = state[r2][c2]
    for r in range(N):
        for c in range(N):
            if state[r][c] == old_s:
                state[r][c] = state[r1][c1]
               
    
    for r in range(N):
        for c in range(N):
            if state[r][c] == state[r1][c1]:
                table[r][c] = new_v
        

def unmerge(r1, c1):
    old_s = state[r1][c1]
    old_v = table[r1][c1]
    for r in range(N):
        for c in range(N):
            if state[r][c] == old_s:
                state[r][c] = (r, c)
                table[r][c] = 'EMPTY'
    table[r1][c1] = old_v
    

def print(r, c):
    answer.append(table[r][c])

def init():
    global answer, table, state, N
    N = 51
    table = [['EMPTY'] * N for _ in range(N)]
    state = [[(r, c)for c in range(N)] for r in range(N)]
    answer = []
    
    
def solution(commands):
    init()
    for command in commands:
        cmd, *p = command.split()
        if cmd == 'UPDATE':
            if len(p) > 2:
                update(int(p[0]), int(p[1]), p[2])
            else:
                replace(*p)
        elif cmd == 'MERGE':
            merge(*map(int, p))
        elif cmd == 'UNMERGE':
            unmerge(*map(int, p))
        elif cmd == 'PRINT':
            print(*map(int, p))
            
    return answer
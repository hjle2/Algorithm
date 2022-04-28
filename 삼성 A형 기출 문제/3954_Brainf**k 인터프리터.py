def getbrinfo(s_c, code):
    que = []
    br = [0] * s_c
    for i, c in enumerate(code):
        if c == '[': que.append(i)
        elif c == ']':
            i_br = que.pop()
            br[i_br] = i
            br[i] = i_br
    return br

def run(i_c):
    global i_m
    global i_i
    i = i_c-1
    cnt = 0
    while i_c < s_c and cnt < 5 * 10 ** 7:
        c = code[i_c]
        if c == '+':
            mem[i_m] += 1
            if mem[i_m] > 255: mem[i_m] = 0
        elif c == '-':
            mem[i_m] -= 1
            if mem[i_m] < 0: mem[i_m] = 255
        elif c == '>':
            i_m += 1
            if i_m == s_m: i_m = 0
        elif c == '<':
            i_m -= 1
            if i_m < 0: i_m = s_m-1
        elif c == ',':
            mem[i_m] = ord(inp[i_i]) if i_i < s_i else 255
            i_i += 1
        elif c == '[':
            if mem[i_m] != 0:
                ret = run(i_c+1)
                if ret: cnt += ret
                else: return
            i_c = br[i_c]
        elif c == ']':
            if mem[i_m] != 0:
                i_c = br[i_c]
            else: return cnt
        i_c += 1
        cnt += 1
    if i_c == s_c:
        return cnt
    else:
        print('Loops', i, br[i])
        return


for _ in range(int(input())):
    s_m, s_c, s_i = map(int, input().split())
    code = input()
    inp = input()
    mem = [0] * s_m
    i_m = i_i = 0
    br = getbrinfo(s_c, code)
    if run(0):
        print('Terminates')

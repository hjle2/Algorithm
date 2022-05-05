def getbr():
    ret = [0]*sc
    q = []
    for i in range(sc):
        if code[i] == '[':
            q.append(i)
        elif code[i] == ']':
            i_br = q.pop()
            ret[i_br], ret[i] = i, i_br
    return ret

def sol(ic):
    i = ic-1
    global im
    global ii
    cnt = 0
    while ic<sc and cnt < 5 * 10 ** 7:
        c = code[ic]
        if c == '+':
            mem[im] += 1
            if mem[im] > 255: mem[im] = 0
        elif c == '-':
            mem[im] -= 1
            if mem[im] < 0: mem[im] = 255
        elif c == '>':
            im += 1
            if im == sm: im = 0
        elif c == '<':
            im -= 1
            if im < 0: im = sm-1
        elif c == ',':
            mem[im] = ord(inp[ii]) if ii<si else 255
            ii += 1
        elif c == '[':
            if mem[im] != 0:
                r = sol(ic+1)
                if r: cnt += r
                else: return
            ic = br[ic]
        elif c == ']':
            if mem[im] != 0:
                ic = br[ic]
            else:
                return cnt
        cnt += 1
        ic += 1
    if ic == sc:
        return cnt
    else:
        print('Loops', i, br[i])
        return

for _ in range(int(input())):
    sm, sc, si = map(int, input().split())
    code = input()
    inp = input()
    mem = [0]*sm
    im = ii = 0
    br = getbr()
    r = sol(0)
    if r: print('Terminates')



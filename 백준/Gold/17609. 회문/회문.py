from copy import deepcopy


def solve(root_flag, txt):
    l, r = 0, len(txt)-1
    flag = False
    while l <= r:
        if txt[l] == txt[r]:
            l += 1
            r -= 1
        elif flag or root_flag:
            return 2
        else:
            flag = True
            if txt[l+1] == txt[r] and txt[l] == txt[r-1]:
                a, b = solve(flag, txt[l+1:r+1]), solve(flag, txt[l:r])
                if a == 0 or b == 0:
                    return 1
                else:
                    return 2
            elif txt[l+1] == txt[r]:
                l += 1
            elif txt[l] == txt[r-1]:
                r -= 1
            else:
                return 2

    if flag:
        return 1
    else:
        return 0


for _ in range(int(input())):
    txt = [*input().rstrip()]
    print(solve(False, txt))


def KMP(full_string, pattern):
    # << kmp table
    n_p = len(pattern)
    table = [0] * n_p
    i = 0
    for j in range(1, n_p):
        while i > 0 and pattern[i] != pattern[j]:
            i = table[i-1]

        if pattern[i] == pattern[j]:
            i += 1
            table[j] = i
            
            
    # kmp
    n_f = len(full_string)
    i = 0
    ret = []
    for j in range(n_f):
        while i > 0 and pattern[i] != full_string[j]:
            i = table[i-1]

        if pattern[i] == full_string[j]:
            i += 1
            if i == len(pattern):
                ret.append(j - i + 1)
                i = table[i-1]
    return ret



def KMP(word, pattern):
    n = len(pattern)
    
    # table 만들기
    table = [0] * n
    i = 0
    for j in range(n):
        while i > 0 and pattern[i] != pattern[j]:
            i = table[i-1]

        if pattern[i] == pattern[j]:
            i += 1
            table[j] = i
    # <<

    # KMP 알고리즘을 이용하여 패턴 찾기
    ret = []
    n = len(word)
    i = 0
    for j in range(n):
        while i > 0 and pattern[i] != word[j]:
            i = table[i-1]
        
        if pattern[i] == word[j]:
            i += 1
            if i == len(pattern):
                ret.append(j - i + 1)
                i = table[i-1]
    # <<
    return ret
    
    

def dfs(inout):
    leng = len(inout)
    if leng == 1:
        return True

    mid = leng // 2

    for i in range(mid):
        if inout[i] == inout[-1-i]:
            return False


    if dfs(inout[:mid]) and dfs(inout[mid+1:]):
        return True
    else:
        return False


for _ in range(int(input())):
    inout = [*input().strip()]

    if dfs(inout):
        print('YES')
    else:
        print('NO')

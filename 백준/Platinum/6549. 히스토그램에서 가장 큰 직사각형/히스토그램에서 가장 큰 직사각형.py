def get_ans():
    ans = 0
    stack = []

    for i, cur_h in enumerate(h):

        if stack and stack[-1][1] > cur_h:
            while stack and stack[-1][1] > cur_h:
                tmp_i, tmp_h = stack.pop()
                # 이 부분 width 를 계산하는 부분이 포인트
                width = i
                if stack:
                    width = i - 1 - stack[-1][0]
                # <<
                square = width * tmp_h
                ans = max(ans, square)

        if not stack or stack[-1][1] <= cur_h:
            stack.append((i, cur_h))

    i = n
    while stack:
        tmp_i, tmp_h = stack.pop()
        width = i
        if stack:
            width = i - 1 - stack[-1][0]
        square = width * tmp_h
        ans = max(ans, square)
    return ans


while True:
    n, *h = map(int, input().split())
    if n == 0:
        break
    print(get_ans())
# 7 2 1 4 5 1 3 3
# 4 1000 1000 1000 1000
# 7 8 7 1 1 1 9 6
# 0

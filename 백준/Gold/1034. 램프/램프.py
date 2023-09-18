N, M = map(int, input().split())
lamp = [[*map(int, [*input()])]for _ in range(N)]
K = int(input())

ans = 0
for i in range(N):
    zero_cnt = 0
    for j in range(M):
        if lamp[i][j] == 0:
            zero_cnt += 1

    tmp = 0
    if zero_cnt <= K and zero_cnt % 2 == K % 2:
        for j in range(N):
            if lamp[i] == lamp[j]:
                tmp += 1
    ans = max(ans, tmp)
print(ans)
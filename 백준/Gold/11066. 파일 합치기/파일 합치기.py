for _ in range(int(input())):
    n = int(input())
    card = [*map(int, input().split())]
    # i 부터 j 까지 합쳤을 때의 값
    dp = [[0] * (n+1) for _ in range(n+1)]

    # 카드들의 누적 합
    S = [0] * (n+1)
    for i in range(1, n+1):
        S[i] = S[i-1] + card[i-1]

    # 몇 개의 카드를 합친 수를 구할 것인지
    for i in range(2, n+1):
        # s 부터 e 카드까지를 합친 최소 값을 구한다
        for s in range(1, n+2-i):
            e = s + i - 1
            # 인덱스 계산이 까다롭고 복잡하다!
            dp[s][e] = min(dp[s][s + k] + dp[s + k + 1][e] for k in range(i-1))
            dp[s][e] += S[e] - S[s-1]
    print(dp[1][-1])

   

### 더 빠르지만 이해하지 못한 풀이
for _ in range(int(input())):
    N = int(input())
    lst = [*map(int, input().split())]
    dp = [[0] * N for _ in range(N+1)]
    ot = [*range(N)]

    for d in range(1, N):
        for s in range(N-d):
            e = s + d
            dp[s][e], ot[s] = min((dp[s][k] + dp[k+1][e], k)for k in range(ot[s], ot[s+1]+1))
            dp[s][e] += sum(lst[s:e+1])
    print(dp[0][-1])

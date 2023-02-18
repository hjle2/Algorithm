# 스택 이용해야 시간초과 통과
N, K = map(int, input().split())
input = [*input()]
ans, k = [], K
for n in input:
    while ans and k > 0 and ans[-1] < n:
        ans.pop()
        k-=1
    ans.append(n)
print(*ans[:N-K], sep='')
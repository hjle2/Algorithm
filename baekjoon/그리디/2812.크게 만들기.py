N, K = map(int, input().split())
ar = [*map(int, [*input().strip()])]

ans, k = [], K
for n in ar:
    while ans and k and ans[-1] < n:
        ans.pop()
        k -= 1
    ans.append(n)

print(*ans[:N-K], sep='')

def get_prime_arr(n):
    ck = [True] * (n+1)
    for i in range(2, n+1):
        if not ck[i]: continue
        m = i * 2
        while m <= n:
            ck[m] = False
            m += i
    ar = []
    for i in range(2, n+1):
        if ck[i]:
            ar.append(i)
    return ar


def solve():
    ans, sum, j = 0, 0, 0
    for i in range(l):
        while j < l and sum < n:
            sum += ar[j]
            j += 1
        if sum == n:
            ans += 1
        sum -= ar[i]
    print(ans)


n = int(input())
# n까지 소수를 모두 구한다
ar = get_prime_arr(n)
l = len(ar)
solve()
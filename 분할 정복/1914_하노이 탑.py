def solve(n, frm, to):
    if n == 1:
        print(frm, to)
        return
    solve(n-1, frm, 6-frm-to)
    print(frm, to)
    solve(n-1, 6-frm-to, to)
N = int(input())
print(2**N-1)
if N <= 20:
    solve(N, 1, 3)
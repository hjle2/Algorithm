N, M = map(int, input().split())
A = [*sorted(map(int, input().split()))]
B = [*sorted(map(int, input().split()))]

a = b = 0
while a < N or b < M:
    if a == N:
        print(B[b], end=' ')
        b += 1
    elif b == M:
        print(A[a], end=' ')
        a += 1
    elif A[a] < B[b]:
        print(A[a], end=' ')
        a += 1
    else:
        print(B[b], end=' ')
        b += 1

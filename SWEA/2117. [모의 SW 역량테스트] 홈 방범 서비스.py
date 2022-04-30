def getcnt(k, r, c):
    cnt = a[r][c]
    for d in range(1, k+1):
        for i in range(-d, d+1):
            nr, nc = r - (d - abs(i)), c + i
            if 0<=nr<n and 0<=nc<n and a[nr][nc]:
                cnt += 1
            if nr != r:
                nr = r - abs(i) + d
                if 0<=nr<n and 0<=nc<n and a[nr][nc]:
                    cnt += 1
    return cnt


def sol():
    ans = 1
    for i in range(1, n+2):
        for r in range(n):
            for c in range(n):
                cnt = getcnt(i, r, c)
                if cnt*m >= (i+1)**2 + i**2:
                    ans = max(ans, cnt)
    return ans

for t in range(int(input())):
    n, m = map(int, input().split())
    a = [list(map(int, input().split()))for _ in range(n)]
    print(f'#{t+1}', sol())
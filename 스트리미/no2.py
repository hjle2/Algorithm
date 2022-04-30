
def getparent(conn, a):
    if conn[a] == a : return a
    else: return getparent(conn, conn[a])

def connect(conn, a, b):
    a, b = getparent(conn, a), getparent(conn, b)
    conn[max(a, b)] = min(a, b)

A = list(map(int, input().split()))
B = list(map(int, input().split()))
N = int(input())
conn = [i for i in range(N)]
cnt = [0]*N
for i in range(len(A)):
    connect(conn, A[i]-1, B[i]-1)
    cnt[getparent(conn, A[i]-1)]+= 1
ans = [0]*N
for i in range(N):
    p = getparent(conn, i)
    ans[p] += cnt[i]
print(max(ans))



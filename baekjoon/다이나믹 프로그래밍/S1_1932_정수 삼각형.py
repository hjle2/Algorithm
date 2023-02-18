N = int(input())
tri = [[int(input())]] + [[*map(int, input().split())]for _ in range(N-1)]
for i in range(1, N):
    for j in range(len(tri[i])):
        tri[i][j] += max(tri[i-1][j] if len(tri[i-1]) > j else 0, tri[i-1][j-1]if j-1 >= 0 else 0)
print(max(tri[-1]))
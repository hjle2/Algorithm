import sys
from collections import deque

input = sys.stdin.readline
dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
n, m, k = map(int, input().split())
ar = [[*map(int, input().split())]for _ in range(n)]
trees = [[deque() for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)
# << input


def spring_summer():
    for i in range(n):
        for j in range(n):
            new_trees = deque()
            dead = 0
            for age in trees[i][j]:
                if ddang[i][j] >= age:
                    ddang[i][j] -= age
                    new_trees.append(age + 1)
                else:
                    dead += age // 2

            trees[i][j] = new_trees
            ddang[i][j] += dead


def fall_winter():
    new_trees = []
    for i in range(n):
        for j in range(n):
            for age in trees[i][j]:
                if age % 5 == 0:
                    for di in range(8):
                        nx, ny = i + dx[di], j + dy[di]
                        if 0 <= nx < n and 0 <= ny < n:
                            new_trees.append((nx, ny))

            ddang[i][j] += ar[i][j]

    for x, y in new_trees:
        trees[x][y].appendleft(1)


ddang = [[5] * n for _ in range(n)]
dead = []
for _ in range(k):
    spring_summer()
    fall_winter()

ans = 0
for i in range(n):
    for j in range(n):
        ans += len(trees[i][j])
print(ans)
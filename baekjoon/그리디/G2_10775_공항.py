# 공항에 1~G 번호의 게이트
# 공항에 P개의 비행기가 순서대로 도착할 예정
# 당신은 i번째 비행기를 1번부터 G번째 게이트 중 하나에 영구적으로 도킹
# 비행기가 도달할 수 있는 게이트가 없다면 공항이 폐쇄되고 어떤 비행기도 도착할 수 없다
# 가장 많은 비행기를 공항에 도킹시켜야 한다 도킹 가능한 최대 비행기의 대수는?

# how to: 특정 게이트로 비행기가 들어오면
# 1번부터 해당 게이트 번호까지 비행기 도킹 가능
# n게이트에 도킹하면, 다음 n게이트로 들어온 비행기는 n-1에 도킹 가능
import sys
input = sys.stdin.readline


def find(x):
    if x == dock[x]: return x
    dock[x] = find(dock[x])
    return dock[x]


G = int(input()) # 공항 게이트의 개수
P = int(input()) # 비행기 대 수
dock = [i for i in range(G+1)]
cnt = 0
for i in range(P):
    n = int(input())
    docking = find(n)
    if docking == 0:
        break
    dock[docking] = dock[docking-1]
    cnt += 1
print(cnt)

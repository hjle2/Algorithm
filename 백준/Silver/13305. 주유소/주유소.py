import sys
input = sys.stdin.readline

n = int(input())
road_len = [*map(int, input().split())]
price = [*map(int, input().split())]

min_fee = 1e9
total_price = 0
for i in range(n-1):
    len = road_len[i]
    fee = price[i]

    min_fee = min(min_fee, fee)
    total_price += min_fee * len
print(total_price)
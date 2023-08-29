import heapq

# N개의 채점기
# url은 도메인/문제ID (10억이하 정수값)
for _ in range(int(input())):
    op, *inp = input().split()
    if op == '100':     # 채점기 준비
        N, u0 = int(inp[0]), inp[1]
    elif op == '200':
        t, p, u = inp
    elif op == '300':
        t = int(inp[0])
    elif op == '400':
        t, J_id = map(int, inp)
    elif op == '500':
        t = int(inp[0])

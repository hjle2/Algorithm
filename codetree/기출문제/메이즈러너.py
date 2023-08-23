N, M, K = map(int, input().split())
board = [[*map(int, input().split())]for _ in range(N)]
people = []
for _ in range(M):
    a, b = map(int, input().split())
    people.append((a-1, b-1))
a, b = map(int, input().split())
exit = (a-1, b-1)


def get_min_square():
    max_square = get_max_square()
    
    for square_size in range(1, max_square+1):
        ret = is_possible(square_size)
        if ret:
            rotate_squre(ret[0], ret[1], ret[2])
    
    
def get_max_square():
    pass


def is_possible(square_size):
    pass


def rotate_squre(sx, sy, size):
    # 회전
    # 출구 위치 찾기
    
    # 내구도 감소
    for x in range(sx, sx + size):
        for y in range(sy, sy + size):
            if board[x][y]:
                board[x][y] -= 1
    

# 최대 벨트 개수
MAX_N = 100000
# 최대 물건 개수
MAX_M = 100000

# 변수
n, m, q = -1, -1, -1

# 물건 정보
prv, nxt = [0] * (MAX_M + 1), [0] * (MAX_M + 1)

# 벨트 정보
head, tail, n_gift = [0] * MAX_N, [0] * MAX_N, [0] * MAX_N


# 100 공장 설립
def build_factory(el):
    # 공장 정보를 입력받습니다.
    n, m = el[1], el[2]

    # 벨트 정보를 만들어줍니다.
    boxes = [[] for _ in range(n)]
    for _id in range(1, m + 1):
        b_num = el[_id + 2]
        b_num -= 1

        boxes[b_num].append(_id)

    # 초기 벨트의 head, tail, nxt, prv값을 설정해줍니다.
    for i in range(n):
        # 비어있는 벨트라면 패스합니다.
        if len(boxes[i]) == 0:
            continue

        # head, tail을 설정해줍니다.
        head[i] = boxes[i][0]
        tail[i] = boxes[i][-1]

        # 벨트 내 선물 총 수를 관리해줍니다.
        n_gift[i] = len(boxes[i])

        # nxt, prv를 설정해줍니다.
        for j in range(len(boxes[i]) - 1):
            nxt[boxes[i][j]] = boxes[i][j + 1]
            prv[boxes[i][j + 1]] = boxes[i][j]


# 200 물건 모두 옮기기
def move(el):
    m_src, m_dst = el[1] - 1, el[2] - 1

    # 옮길게 없음
    if n_gift[m_src] == 0:
        print(n_gift[m_dst])
        return

    if n_gift[m_dst] == 0:
        tail[m_dst] = tail[m_src]

    else:
        prv[head[m_dst]] = tail[m_src]
        nxt[tail[m_src]] = head[m_dst]

    head[m_dst] = head[m_src]
    head[m_src] = tail[m_src] = 0

    # n_gift
    n_gift[m_dst] += n_gift[m_src]
    n_gift[m_src] = 0

    print(n_gift[m_dst])


def remove_head(idx):
    if n_gift[idx] == 0:
        return 0

    elif n_gift[idx] == 1:
        i_gift = head[idx]
        head[idx] = tail[idx] = 0
        n_gift[idx] = 0
        return i_gift

    else:
        i_remove = head[idx]
        i_new = nxt[i_remove]

        head[idx] = i_new
        nxt[i_remove] = prv[i_new] = 0
        n_gift[idx] -= 1

        return i_remove


def push_head(idx, i_gift):
    if i_gift == 0:
        return

    if n_gift[idx] == 0:
        tail[idx] = i_gift
    else:
        old_head = head[idx]
        nxt[i_gift] = old_head
        prv[old_head] = i_gift

    head[idx] = i_gift
    n_gift[idx] += 1


# 300 앞 물건만 교체하기
def change(el):
    m_src, m_dst = el[1] - 1, el[2] - 1

    src_head = remove_head(m_src)
    dst_head = remove_head(m_dst)
    push_head(m_dst, src_head)
    push_head(m_src, dst_head)

    print(n_gift[m_dst])


# 400 물건 나누기
def divide(el):
    m_src, m_dst = el[1] - 1, el[2] - 1

    if n_gift[m_src] < 2:
        print(n_gift[m_dst])
        return

    n_div = n_gift[m_src] // 2
    tmp_gifts = []
    for _ in range(n_div):
        tmp_gifts.append(remove_head(m_src))

    for i_gift in tmp_gifts[::-1]:
        push_head(m_dst, i_gift)

    print(n_gift[m_dst])


# 500 선물 정보 얻기
def gift_score(el):
    p_num = el[1]

    a = prv[p_num] if prv[p_num] != 0 else -1
    b = nxt[p_num] if nxt[p_num] != 0 else -1

    print(a + 2 * b)


# 600 벨트 정보 얻기
def belt_score(el):
    b_num = el[1] - 1

    a = head[b_num] if head[b_num] != 0 else -1
    b = tail[b_num] if tail[b_num] != 0 else -1
    c = n_gift[b_num]

    print(a + 2 * b + 3 * c)


# 입력:
for _ in range(int(input())):
    elems = [*map(int, input().split())]
    q_type = elems[0]

    if q_type == 100:
        build_factory(elems)
    elif q_type == 200:
        move(elems)
    elif q_type == 300:
        change(elems)
    elif q_type == 400:
        divide(elems)
    elif q_type == 500:
        gift_score(elems)
    else:
        belt_score(elems)


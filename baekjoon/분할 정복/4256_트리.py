def getPostOrder(preor, inor):
    if len(preor) == 0:
        return []
    if len(preor) == 1:
        return preor
    ret = []
    top = preor[0]
    idx = inor.index(top)
    ret += getPostOrder(preor[1:idx+1], inor[:idx])
    ret += getPostOrder(preor[idx+1:], inor[idx+1:])
    return ret + [top]


T = int(input())
for _ in range(T):
    n = int(input())
    preor = [*map(int, input().split())]
    inor = [*map(int, input().split())]
    print(*getPostOrder(preor, inor))


# inor 의 마지막은 top 의 오른쪽 노드
# inor 의 첫번째는 맨 왼쪽의 노드

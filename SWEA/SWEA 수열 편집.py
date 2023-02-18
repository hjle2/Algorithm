for tc in range(int(input())):
    N, M, L = map(int, input().split())
    # 수열 길이, 추가 횟수, 출력할 인덱스 번호

    ar = [*map(int, input().split())]
    # 초기 수열

    for _ in range(M):
        cmd = input().split()
        if cmd[0] == 'I':
            ar.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == 'D':
            ar.remove(ar[int(cmd[1])])
        elif cmd[0] == 'C':
            ar[int(cmd[1])] = int(cmd[2])
        print(ar)
    if L < len(ar):
        print(f'#{tc+1}', ar[L])
    else:
        print(f'#{tc+1}', -1)

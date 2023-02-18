import sys
input = sys.stdin.readline

N, K = map(int, input().split())
appliance = [*map(int, input().split())]

cnt = 0
tab = []
for i, app in enumerate(appliance):
    # 이미 멀티탭에 꽂혀 있으면
    if app in tab:
        continue
    # 멀티탭에 빈 공간이 있으면
    if len(tab) < N:
        tab.append(app)
        continue

    next_app = []
    used = True

    for tab_app in tab:
        if tab_app in appliance[i:]:
            idx = appliance[i:].index(tab_app)
        # 다시 사용되지 않는 전자제품의 탭을 구해서 뽑는다
        else:
            idx = 101
            used = False
        next_app.append(idx)

        if not used:
            break

    nxt = next_app.index(max(next_app))
    del tab[nxt]
    tab.append(app)
    cnt += 1
print(cnt)
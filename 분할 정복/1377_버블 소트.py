# N = int(input())
# A = [[int(input()), i] for i in range(N)]
# A.sort()
# print(max(A[i][1]-i for i in range(N))+1)


# 숏 코딩 파이썬으로 통과
N = int(input())
A = [int(input())for _ in range(N)]
# 와 이걸 몰랐네..
# 배열을 반복문에서 순회할 때, 변수를 하나 추가하면 인덱스를 확인 할 수 있따..
# 그리고 이거를 [i, j] 로 sorted 를 걸어주면..!
# 이렇게 배열이 된다...!!!!
# sorted[j, i] for i, j in enumerate(A)

# enumerate !!
# enumerate(배열) 은
# 인덱스, 배열의 인덱스 값!!!!
E = enumerate

print(max(j[1]-i for i, j in E(sorted([j, i]for i,j in E(A))))+1)

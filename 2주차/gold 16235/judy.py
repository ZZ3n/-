N, M, K = map(int, input().split())

# 양분
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

H = [[5] * N for _ in range(N)]

# 나무
B = [[[] for _ in range(N)] for _ in range(N)]
for i in range(M):
    row, col, namu = map(int, input().split())
    B[row-1][col-1].append(namu) # 나무 심기

def spring_summer():
    number = 0
    deaf = []
    for row in range(N):
        for col in range(N):
            B[row][col].sort()  # 나무를 나이에 따라 정렬
            alive = []
            dead = 0
            for age in B[row][col]:
                if H[row][col] >= age:
                    H[row][col] -= age  # 나무가 양분을 소비
                    alive.append(age + 1)  # 나이 증가
                    number += 1
                else:
                    dead += age // 2  # 죽은 나무는 양분이 됨
            B[row][col] = alive
            deaf.append([row,col,dead])
    for q in deaf:
        H[q[0]][q[1]] += q[2]  # 죽은 나무가 양분으로 반환됨
    return number


def autumn_winter():
    for row in range(N):
        for col in range(N):
            if any(age % 5 == 0 for age in B[row][col]):
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == 0 and j == 0 or not (0 <= row + i < N and 0 <= col + j < N):
                            continue
                        B[row + i][col + j].append(1)  # 새로운 나무가 생김
    for i in range(N):
        for j in range(N):
            H[i][j] += A[i][j]  # 겨울에는 양분을 추가


namus = 0
for _ in range(K):
    namus = spring_summer()
    autumn_winter()


print(namus)
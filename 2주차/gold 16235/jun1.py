# 나무 재테크 

# 부동산 투자로 돈 벌어서 N x N 크기의 땅 구매함.
# 쉬운 땅 관리를 위해서 땅을 1 x 1 로 나누어 놓았음.
# 각 칸의 좌표는 (r, c) 로 나타낸다. 
# r 은 가장 위에서부터 떨어진 칸의 갯수
# c 는 가장 왼쪽으로부터 떨어진 칸의 갯수
# r과 c는 1부터 시작한다. 
# 땅의 양분을 조사하는 로봇으로 1 x 1 크기의 칸에 들어있는 양분 조사
# 모든 칸에 대해서 조사를 한다. 가장 처음엔 양분은 모든 칸에 5만큼 들어있다. 

# 이 땅에 나무를 심고 키워서 파는 나무 재테크를 할 것이다. 
# M 개의 나무를 구매해서 심었다. 같은 1 x 1 크기의 칸에 여러 개의 나무가 심어져 있을 수도 있다.
# 나무는 사계절을 보낸다.

# 1. 봄 
# 나무가 자신의 나이만큼 양분을 먹고 나이가 1증가한다. 
# 각각의 나무는 자기가 있는 1 x 1 칸의 양분만 먹는다.
# 하나의 칸에 여러 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다. 
# 만약, 땅에 양분이 부족해서 자신의 나이만큼 먹을 수 없다면 즉시 죽는다.

# 2. 여름
# 봄에 죽은 나무가 양분으로 변한다. 
# 각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다.
# 소수점 아래는 버린다

# 3. 가을 
# 나무가 번식한다. 
# 번식하는 나무는 나이가 5의 배수이어야하며, 인접한 8개의 칸에는 나이가 1인 나무가 생긴다.
# 어떤 칸 (r,c) 와 인접한 칸인 (r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1) 이다.
# 땅을 벗어나는 칸에는 나무가 생기지 않는다.

# 4. 겨울
# 로봇이 돌아다니면서 땅에 양분을 추가한다. 
# 각 칸에 추가되는 양분의 양은 A[r][c] 이며 입력으로 주어진다.

# K 년이 지난 후 땅에 살아있는 나무 갯수를 구하는 프로그램을 작성하여라.

# 입력으로 첫째 줄에는 N, M, K 가 주어진다.
# 각각은 땅의 크기, 심는 나무 갯수, 어느 년도가 지났는 가
# 둘째 줄부터 N개의 줄에 A 배열의 값이 주어진다. r번째 줄의 c번째 값은 A[r][c] 이다.
# 이는 r,c 칸에 겨울에 줄 양분이다.
# 다음 M개의 줄에는 심은 나무의 정보를 나타내는 세 정수 x,y,z가 주어진다.
# x, y 는 나무를 심을 위치, z 는 나이를 의미한다.

import sys
from collections import defaultdict
input = sys.stdin.read
# 모든 입력을 받기
data = input().split()

index = 0 
N = int(data[index])
M = int(data[index + 1])
K = int(data[index + 2])
index += 3
A = []
for i in range(N):
    A.append(list(map(int, data[index:index + N])))
    index += N

tree_info = []
for j in range(M):
    x = int(data[index])
    y = int(data[index + 1])
    z = int(data[index + 2])
    tree_info.append((x, y, z))
    index += 3

# 입력 잘됬는지 확인하는 출력
# print("N, M, K =", N, M, K)
# print("A[r, c] =")
# for row in A:
#     print(row)
# print("심을 나무의 정보를 담은 배열:")
# for info in tree_info:
#     print("(x, y, z) =", info[0], info[1], info[2])

# 나무 정보를 관리하기 위해 딕셔너리로 만들자
# 키는 위치로 (x,y), 값 : x,y 위치에 있는 나무 나이 리스트
# 나무 정보를 관리할 defaultdict 사용, 나무를 위치별로 그룹화
trees = defaultdict(list)
for x, y, age in tree_info:
    trees[(x - 1, y - 1)].append(age)

# 나무 리스트를 나이순으로 정렬
for pos in trees:
    trees[pos].sort()

# 초기 양분 배열 설정, 모든 칸에 양분 5
nutrients = [[5] * N for _ in range(N)]

# 나무 번식 방향 설정, 8방향
directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

for _ in range(K):
    # 각 계절의 작업을 시작, 봄에서 죽은 나무를 여름에 양분으로 변환
    dead_trees = defaultdict(int)
    for pos in list(trees):
        alive = []
        dead = 0
        for age in trees[pos]:
            if nutrients[pos[0]][pos[1]] >= age:
                nutrients[pos[0]][pos[1]] -= age
                alive.append(age + 1)
            else:
                dead += age // 2
        trees[pos] = alive
        nutrients[pos[0]][pos[1]] += dead

    # 가을에는 번식 가능한 나무가 인접 칸에 새로운 나무를 생성
    new_trees = defaultdict(list)
    for pos, ages in trees.items():
        for age in ages:
            if age % 5 == 0:
                for dx, dy in directions:
                    nx, ny = pos[0] + dx, pos[1] + dy
                    if 0 <= nx < N and 0 <= ny < N:
                        new_trees[(nx, ny)].append(1)
    
    # 새로운 나무를 기존 리스트에 추가하고 정렬
    for pos, new_ages in new_trees.items():
        trees[pos].extend(new_ages)
        trees[pos].sort()

    # 겨울에 각 칸에 양분 추가
    for i in range(N):
        for j in range(N):
            nutrients[i][j] += A[i][j]

# K년 후 살아있는 나무의 총 수 계산
live_tree_count = sum(len(ages) for ages in trees.values())
print(live_tree_count)

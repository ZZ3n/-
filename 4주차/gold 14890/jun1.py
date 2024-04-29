def can_pass(line, N, L):
    # 사용된 경사로 위치를 추적하는 배열
    used = [False] * N
    
    for i in range(N - 1):
        if line[i] == line[i + 1]:
            continue  # 같은 높이의 칸은 경사로가 필요 없으므로 계속 진행
        elif abs(line[i] - line[i + 1]) > 1:
            return False  # 높이 차이가 1보다 크면 경사로로 연결 불가능

        # 오르막 경사로 설치 조건 검사
        elif line[i] < line[i + 1]:
            # L 길이만큼의 여유 공간이 없거나 이미 경사로가 설치된 경우 실패
            if i + 1 < L or any(used[i - j] for j in range(L)):
                return False
            # L 길이 전의 칸들의 높이가 모두 같아야 하며, 해당 칸들에 경사로가 설치되지 않았어야 함
            if any(line[i] != line[i - j] for j in range(1, L)):
                return False
            # 오르막 경사로 설치를 위한 칸 표시
            for j in range(L):
                used[i - j] = True

        # 내리막 경사로 설치 조건 검사
        elif line[i] > line[i + 1]:
            # L 길이만큼의 여유 공간이 없거나 이미 경사로가 설치된 경우 실패
            if i + L >= N or any(used[i + j + 1] for j in range(L)):
                return False
            # 내리막 경사로가 설치될 칸들의 높이가 모두 같아야 함
            if any(line[i + 1] != line[i + j + 1] for j in range(L)):
                return False
            # 내리막 경사로 설치를 위한 칸 표시
            for j in range(L):
                used[i + j + 1] = True
    return True

def count_passable_paths(grid, N, L):
    count = 0
    # 각 행에 대해 경로를 확인
    for i in range(N):
        if can_pass(grid[i], N, L):
            count += 1
    # 각 열에 대해 경로를 확인
    for j in range(N):
        col = [grid[i][j] for i in range(N)]
        if can_pass(col, N, L):
            count += 1
    return count

# 사용자 입력을 받는 부분
N, L = map(int, input().split())
grid = []
for _ in range(N):
    row = list(map(int, input().split()))
    grid.append(row)

# 함수를 실행하고 결과를 출력하는 부분
result = count_passable_paths(grid, N, L)
print(result)

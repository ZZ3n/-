"""
+ : 뒤로 L개 칸이 모두 같은 높이인지 확인
- : 앞으로 L개 칸이 모두 같은 높이인지 확인
이미 경사로가 설치된 위치나, 칸의 높이가 다른 경우 길을 지나갈 수 없다.
"""

# 입력받기
N, L = map(int, input().split())
JIDO = []
for i in range(N):
    JIDO.append(list(map(int, input().split())))

def check_road(road, L):
    n = len(road)
    used = [False] * n  # 경사로 설치 여부

    for i in range(n - 1):
        if road[i] == road[i + 1]: # 연속된 같은 높이
            continue
        elif abs(road[i] - road[i + 1]) > 1: # 높이가 달라질 경우 (1보다 틀 때)
            return False
        elif road[i] > road[i + 1]: # 경사로가 낮아질 경우 (차이가 1일 때)
            temp = road[i + 1]
            for j in range(i + 1, i + 1 + L): #경사로 부분 확인
                if j >= n or road[j] != temp or used[j]:
                    return False #경사로 설치 못하면 빠꾸
                used[j] = True #경사로 설치
        elif road[i] < road[i + 1]: # 경사로가 높아질 경우 (차이가 1일 때)
            temp = road[i]
            for j in range(i, i - L, -1): #경사로 부분 확인
                if j < 0 or road[j] != temp or used[j]:
                    return False #경사로 설치 못하면 빠꾸
                used[j] = True #경사로 설치
    return True


def solve(N, L, grid):
    result = 0
    for i in range(N):
        if check_road([grid[i][j] for j in range(N)], L): #ROW
            result += 1
        if check_road([grid[j][i] for j in range(N)], L): #COL
            result += 1
    return result

print(solve(N, L, JIDO))
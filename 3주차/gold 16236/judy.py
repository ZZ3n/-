"""
0: 빈 칸
1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
9: 아기 상어의 위치
"""

from collections import deque


def bfs(N, grid, start_r, start_c):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    shark_size = 2
    shark_eat = 0
    time_spent = 0
    queue = deque([(start_r, start_c, 0)])  # (row, col, time)
    grid[start_r][start_c] = 0

    while True:
        possible_fishes = []
        visited = [[False] * N for _ in range(N)]
        while queue:
            r, c, time = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                    visited[nr][nc] = True
                    if grid[nr][nc] <= shark_size:  # 상어가 지나갈 수 있음
                        queue.append((nr, nc, time + 1))
                        if 0 < grid[nr][nc] < shark_size:  # 먹을 수 있는 물고기
                            possible_fishes.append((nr, nc, time + 1))

        if not possible_fishes:
            break  # 먹을 수 있는 물고기가 없으므로 종료

        # 가능한 물고기 중 가장 가까운 물고기 선택
        possible_fishes.sort(key=lambda x: (x[2], x[0], x[1]))  # 거리, 행, 열 순으로 정렬
        nr, nc, nt = possible_fishes[0]
        grid[nr][nc] = 0  # 물고기 먹기
        time_spent += nt
        shark_eat += 1
        if shark_eat == shark_size:
            shark_size += 1
            shark_eat = 0
        queue = deque([(nr, nc, 0)])  # 새로운 위치에서 BFS 시작

    return time_spent


# 입력 받기
N = int(input())
grid = []
shark_r, shark_c = 0, 0
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        if row[j] == 9:
            shark_r, shark_c = i, j  # 아기 상어의 초기 위치
            row[j] = 0  # 아기 상어의 시작 위치를 빈 칸으로 변경
    grid.append(row)

# 결과 출력
print(bfs(N, grid, shark_r, shark_c))

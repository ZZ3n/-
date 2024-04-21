from collections import deque

def bfs(start, grid, size, n):
    # 방향 벡터 설정 (상, 좌, 우, 하)
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    # BFS를 위한 큐 초기화 및 시작점 등록
    queue = deque([(start[0], start[1], 0)])  # (row, col, distance)
    # 방문 체크 배열 초기화
    visited = [[False] * n for _ in range(n)]
    visited[start[0]][start[1]] = True
    # 먹을 수 있는 물고기 리스트
    eatable_fish = []
    
    # BFS 실행
    while queue:
        r, c, dist = queue.popleft()
        
        # 가능한 모든 방향으로 탐색
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                if grid[nr][nc] <= size:  # 이동 가능 조건
                    visited[nr][nc] = True
                    if 0 < grid[nr][nc] < size:  # 먹을 수 있는 물고기 조건
                        eatable_fish.append((dist + 1, nr, nc))
                    queue.append((nr, nc, dist + 1))
    
    # 먹을 수 있는 가장 가까운 물고기 반환
    if eatable_fish:
        eatable_fish.sort()
        return eatable_fish[0]
    return None

n = int(input().strip())
grid = [list(map(int, input().split())) for _ in range(n)]

shark_size = 2 #초기 아기 상어 사이즈
eaten = 0 #먹은 물고기 수 
time = 0 #총 지난 시간 

#아기 상어 초기 위치 찾기
shark_pos = None
for i in range(n):
    for j in range(n):
        if grid[i][j] == 9:
            shark_pos = (i,j)
            grid[i][j] = 0 #상어 위치 초기화
            break
    if shark_pos:
        break

while True: #먹을 수 있는 물고기가 없을 때 까지 반복
    result = bfs(shark_pos, grid, shark_size, n)
    if not result:
         break
    dist, fish_r, fish_c = result
    # 물고기 먹기
    grid[fish_r][fish_c] = 0
    shark_pos = (fish_r, fish_c)
    time += dist
    eaten += 1
        
    # 성장 조건 체크
    if eaten == shark_size:
        shark_size += 1
        eaten = 0

print(time)
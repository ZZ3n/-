'''
NxN 크기의 공간, 물고기 M 마리, 아기 1마리
1칸 당 물고기 1마리
처음 아기 = 2
움직임 = 1
자신의 크기보다 크면 => 못 감
작으면 => 먹음

먹을 수 있는 물고기가 없다면, -> 도움 -> 종료
1마리라면 -> 그거
1마리 초과 -> 가까운 물고기 (*가까운 물고기 = 지나야 하는 칸의 개수가 최솟값, Top -> Left)
이동 -> 1초
크기 당 1마리 먹어야 함.

# 해야 하는 일
BFS로 접근.
큐 방식

# 알게
'''
from queue import PriorityQueue

N = int(input())
field = []
for i in range(N):
    field.append(list(map(int, input().split())))

SHARK = 9
SHARK_SIZE = 2
SHARK_STOMACH = 0


def where_shark():
    for r in range(N):
        try:
            c = field[r].index(SHARK)
        except ValueError:
            continue
        return r, c


def eat(nx, ny):
    global SHARK_SIZE
    global SHARK_STOMACH
    global field

    field[nx][ny] = 0
    SHARK_STOMACH += 1
    if SHARK_SIZE == SHARK_STOMACH:
        SHARK_SIZE += 1
        SHARK_STOMACH = 0


# d 가 1순위, 그 다음이 r
def hunt(r, c):
    global SHARK_SIZE
    global SHARK_STOMACH
    global SHARK
    global field

    PQ = PriorityQueue()
    PQ.put((0, r, c))
    visited = set()
    visited.add((r, c))
    field[r][c] = 0

    while not PQ.empty():
        nd, nx, ny = PQ.get()
        fish_size = field[nx][ny]
        if fish_size < SHARK_SIZE and fish_size != 0:
            eat(nx, ny)
            return nx, ny, nd
        for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            x, y, d = nx + dx, ny + dy, nd + 1
            if x < 0 or x >= N or y < 0 or y >= N:
                continue
            fish_size = field[x][y]
            if (x, y) in visited:
                continue
            if fish_size == 0 or fish_size <= SHARK_SIZE:
                visited.add((x, y))
                PQ.put((d, x, y))
                continue
            if fish_size > SHARK_SIZE:
                visited.add((x, y))
                continue
    return r, c, 0


sx, sy = where_shark()
result = 0
while True:
    sx, sy, sd = hunt(sx, sy)
    result += sd
    if sd == 0:
        break
print(result)

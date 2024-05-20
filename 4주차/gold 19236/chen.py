"""
4x4 x,y 1칸 -> 물고기 1 마리(번호, 방향)
번호 : 1 <= 번호 <= 16, 같은 번호는 없다.
방향 : 8방향
(0,0)에서 물고기를 먹고, (0,0)에 존재

물고기 턴
번호가 작은 물고기 부터 이동
    이동할 수 있는 칸
        빈칸, 다른 물고기가 있는 칸
    이동할 수 없는 칸
        상어가 있는 칸, 공간의 경계를 넘는 칸
    while(이동할 수 없으면)
        반시계 방향으로 45도 회전
        그래도 이동할 수 없으면
            이동하지 않는다.
            이동할 수 없는 경우에 화살표는 어떻게 되는가?
    if (이동 할 수 있으면)
        다른 물고기가 있는 경우
            서로 자리를 바꾼다.
        다른 물고기가 없는 경우
            이동한다.

상어 턴
한 번에 여러 칸을 이동할 수 있다.
방향에 있는 물고기가 있는 칸 중 하나로 간다.
    물고기가 있는 칸에 가면
        물고기를 먹고, 방향을 갖는다.
만약 이동할 수 없으면 -> 종료
이동했다면 -> 다시 물고기 턴.

BFS 문제
"""
N = 4
DIRECTIONS = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
MAP = list([] for i in range(N))
for i in range(N):
    input_line = list(map(int, input().split()))
    for j in range(N):
        idx = j * 2
        elem = (input_line[idx], input_line[idx + 1] - 1)
        MAP[i].append(elem)

SHARK_NUM = 99
EMPTY_NUM = 77
ALIVE_FISHES = [i + 1 for i in range(N * N)]
SUM = 102


def get_direction(M, y, x):
    return M[y][x][1]


def get_number(M, y, x):
    return M[y][x][0]


def go_SHARK(M, y, x):
    return SHARK_NUM, get_direction(M, y, x)


def fish_turn(M, alive_fishes):
    global SHARK_NUM
    for fish_num in alive_fishes:
        move_flag = True
        for y in range(N):
            if not move_flag:
                break
            for x in range(N):
                if not move_flag:
                    break
                if M[y][x][0] == fish_num:
                    direction = M[y][x][1]
                    for i in range(8):
                        idx = (direction + i) % 8
                        n_y = y + DIRECTIONS[idx][0]
                        n_x = x + DIRECTIONS[idx][1]
                        if 0 <= n_y < N and 0 <= n_x < N and M[n_y][n_x][0] != SHARK_NUM:
                            M[n_y][n_x], M[y][x] = (M[y][x][0], idx), M[n_y][n_x]
                            move_flag = False
                            break
                        else:
                            continue
    return M


def shark_turn(M, alive_fishes, sy, sx, score):
    global N
    global SUM
    direc_y, direc_x = DIRECTIONS[M[sy][sx][1]]
    results = list([score])
    for i in range(1, N + 1):
        ny, nx = sy + direc_y * i, sx + direc_x * i
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            #print("Nah")
            break
        if M[ny][nx][0] == EMPTY_NUM:
            # print("EMPTY")
            continue
        # print(f"move to ({ny},{nx})")
        m = new_map(M)
        fish = alive_fishes.index(m[ny][nx][0])
        new_fishes = alive_fishes[:fish] + alive_fishes[fish + 1:]
        new_score = score + m[ny][nx][0]
        m[ny][nx] = (SHARK_NUM, m[ny][nx][1])
        m[sy][sx] = (EMPTY_NUM, m[sy][sx][1])
        results.append(BFS(m, new_fishes, ny, nx, new_score))
    # print(results)
    return max(results)


def new_map(M):
    m = list([] for i in range(N))
    for i in range(N):
        for j in range(N):
            m[i].append(M[i][j])
    return m


def print_M(M, alive_fishes, msg):
    print(f"{msg} ####### MAP ###### : {alive_fishes}")

    def print_directions(d):
        ds = ['↑', '↖', '←', '↙', '↓', '↘', '→', '↗']
        return ds[d]

    for lane in M:
        for elem in lane:
            direction = print_directions(elem[1])
            if elem[0] == SHARK_NUM:
                print(f'(🦈,{direction})', end='\t')
            elif elem[0] == EMPTY_NUM:
                print(f'(❌,{direction})', end='\t')
            else:
                print(f'({elem[0]},{direction})', end='\t')
        print('')





def BFS(M, alive_fishes, sy, sx, score):
    # print_M(M, alive_fishes, "before fish_turn")
    M = fish_turn(M, alive_fishes)
    # print_M(M, alive_fishes, "after fish_turn")
    return shark_turn(M, alive_fishes, sy, sx, score)


init_fish = ALIVE_FISHES.index(MAP[0][0][0])
init_alive_fishes = ALIVE_FISHES[:init_fish] + ALIVE_FISHES[init_fish + 1:]
MAP[0][0] = (SHARK_NUM, MAP[0][0][1])

answer = BFS(MAP, init_alive_fishes, 0, 0, init_fish)
print(answer+1)

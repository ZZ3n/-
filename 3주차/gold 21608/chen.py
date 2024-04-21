'''
교실 : NxN
다니는 학생 : 1 ~ N^2
각 학생 당 좋아하는 학생 수 : 4명
한 칸당 한명
## 규칙 ##
1. 인접 칸 중 좋아하는 학생이 많은 자리
2. 여러 개이면, 비어 있는 칸이 가장 많은 자리
3. r이 가장 작은 칸 => c가 가장 작은 칸
## 결과 ##
학생 1당 인접한 좋아하는 학생 수 = 1

## 전략 ##
처음 -> 그냥 1,1에 앉힌다.

like_mate in classroom?
 y>
    -> travel(adj(like_mates in classroom))
        -> pq.put((like, empty, r, c))
    -> if pq is empty
        -> next case
    -> else
        -> pq.get()
 n>
    -> full_travel()
        -> pq.put((like,empty,r,c))
    -> pq.get()
'''
N = int(input())
student_dict = {}
for _ in range(N * N):
    row = list(map(int, input().split()))
    student_dict[row[0]] = row[1:]

classroom = [[0 for _ in range(N)] for _2 in range(N)]


def cal_adj_score(x, y, mates):
    global classroom
    mate_cnt = 0
    empty_cnt = 0
    D = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for dx, dy in D:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if classroom[nx][ny] in mates:
            mate_cnt += 1
        if classroom[nx][ny] == 0:
            empty_cnt += 1
    return mate_cnt, empty_cnt


def cal_score():
    global classroom
    global N
    result = 0
    for r in range(N):
        for c in range(N):
            s = classroom[r][c]
            m_score, e, = cal_adj_score(r, c, student_dict[s])
            if m_score == 0: result += 0
            if m_score == 1: result += 1
            if m_score == 2: result += 10
            if m_score == 3: result += 100
            if m_score == 4: result += 1000
    return result


def find_pos(mates):
    global N
    global classroom
    hubo = (-1, -1, -1, -1)
    for r in range(N):
        for c in range(N):
            if classroom[r][c] != 0: continue
            m, e = cal_adj_score(r, c, mates)

            if m > hubo[0]:
                hubo = (m, e, r, c)
                continue
            if m < hubo[0]: continue

            if e > hubo[1]:
                hubo = (m, e, r, c)
                continue
            if e < hubo[1]: continue

            if r < hubo[2]:
                hubo = (m, e, r, c)
                continue
            if r > hubo[2]: continue

            if c < hubo[3]:
                hubo = (m, e, r, c)
                continue
            if c > hubo[3]: continue

    return hubo[2], hubo[3]


for student, mates in student_dict.items():
    x, y = find_pos(mates)
    classroom[x][y] = student
print(cal_score())

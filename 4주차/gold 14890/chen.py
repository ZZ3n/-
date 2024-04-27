N, L = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]


def make_ramp(lane):
    global MAP, N, L
    ramp_list = list()
    flat = True
    for e in lane:
        if e != lane[0]:
            flat = False
    if flat: return True

    for idx, elem in enumerate(lane):
        if idx - 1 >= 0:
            diff = lane[idx] - lane[idx - 1]
            if diff > 1:  # 경사가 너무 크다
                return False
            if diff == 1 and (idx - L) < 0:  # 경사를 지을 수 없다.
                return False
            if diff == 1 and (idx - L) >= 0:
                temp = []
                for j in range(idx - L, idx):
                    before = lane[j]
                    temp.append(j)
                    if j in ramp_list:  ## 경사 겹침
                        return False
                    if (elem - before) != 1:  ## 경사 못 지음
                        return False
                ramp_list.extend(temp)

        if idx + 1 < N:
            diff = lane[idx] - lane[idx + 1]
            if diff > 1:  # 경사가 너무 크다
                return False
            if diff == 1 and (idx + L) >= N:  # 경사로 못 짓는다.
                return False
            if diff == 1 and (idx + L) < N:
                temp = []
                for j in range(idx + 1, idx + L + 1):
                    after = lane[j]
                    temp.append(j)
                    if j in ramp_list:  ## 경사 겹침
                        return False
                    if (elem - after) != 1:  ## 경사 못 지음
                        return False
                ramp_list.extend(temp)
    return True


result = 0
for i in range(N):
    horizon = make_ramp([MAP[i][j] for j in range(N)])
    vertical = make_ramp([MAP[j][i] for j in range(N)])
    if horizon: result += 1
    if vertical: result += 1

# print(N, L)
# print(MAP)
print(result)

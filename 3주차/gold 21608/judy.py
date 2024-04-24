def calculate_satisfaction(N, classroom, fav_list):
    satisfaction = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for r in range(N):
        for c in range(N):
            student = classroom[r][c]
            count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and classroom[nr][nc] in fav_list[student]:
                    count += 1
            if count > 0:
                satisfaction += 10 ** (count - 1)

    return satisfaction


def place_student(N, classroom, student, fav_students):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    best_r, best_c = -1, -1
    max_fav, max_empty = -1, -1

    for r in range(N):
        for c in range(N):
            if classroom[r][c] == 0:
                fav_count, empty_count = 0, 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < N:
                        if classroom[nr][nc] in fav_students:
                            fav_count += 1
                        if classroom[nr][nc] == 0:
                            empty_count += 1

                if (fav_count > max_fav) or (fav_count == max_fav and empty_count > max_empty) or (
                        fav_count == max_fav and empty_count == max_empty and r < best_r) or (
                        fav_count == max_fav and empty_count == max_empty and r == best_r and c < best_c):
                    best_r, best_c = r, c
                    max_fav, max_empty = fav_count, empty_count

    classroom[best_r][best_c] = student


N = int(input())
classroom = [[0] * N for _ in range(N)]
fav_list = {}

for _ in range(N * N):
    data = list(map(int, input().split()))
    student, fav_students = data[0], data[1:]
    fav_list[student] = fav_students
    place_student(N, classroom, student, fav_students)

print(calculate_satisfaction(N, classroom, fav_list))

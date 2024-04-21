n = int(input()) # 교실 크기 
data = [[0] * n for _ in range(n)] # 교실 격자 초기화 
students = [list(map(int, input().split())) for _ in range(n**2)] # 각 학생과 좋아하는 학생 4명 번호 저장

#상하 좌우 움직일때 좌표 미리 저장
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for student in students:
    available = []
    for i in range(n):
        for j in range(n):
            if data[i][j] == 0: #현재 선택 격자가 비었다면
                # 각 칸마다 좋아하는 학생수, 빈자리 수를 계산
                prefer, empty = 0, 0
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if data[nx][ny] in student[1:]:
                            prefer += 1
                        if data[nx][ny] == 0:
                            empty += 1
                #계산된 결과를 available 리스트에 저장된다.
                available.append([i,j,prefer,empty])
    #계산된 결과를 정렬
    #좋아하는 학생 수(내림차순), 빈 칸 수(내림차순), 행 번호(오름차순), 열 번호(오름차순)      
    available.sort(key=lambda x: (-x[2], -x[3], x[0], x[1]))  
    #최적의 자리에 학생 번호를 배치한다.   
    data[available[0][0]][available[0][1]] = student[0]

answer = 0
#만족도 점수 배열 0~4명 좋아하는 학생 수에 따라 다음
score = [0,1,10,100,1000]
students.sort()
for i in range(n):
    for j in range(n):
        count = 0
        for k in range(4):
            #인접한 좌표를 돌면서 좋아하는 학생 수 판별 
            nx, ny = i + dx[k], j + dy[k] 
            if 0 <= nx < n and 0 <= ny < n: 
                if data[nx][ny] in students[data[i][j] - 1][1:]:
                    count += 1
        answer += score[count] 
print(answer)

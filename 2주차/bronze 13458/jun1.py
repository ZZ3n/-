import sys
input = sys.stdin.read

# 입력 받기
data = input().split()
N = int(data[0])  # 시험장의 개수
A = list(map(int, data[1:N+1]))  # 각 시험장의 응시자 수
B, C = map(int, data[N+1:])  # B: 총감독관 감시 가능 인원, C: 부감독관 감시 가능 인원

# 결과 계산
result = N  # 각 시험장마다 최소 1명의 총감독관 필요
for i in range(N):
    remaining = A[i] - B  # 총감독관이 감시 후 남은 응시자 수
    if remaining > 0:  # 남은 응시자가 있으면 부감독관 배치
        result += (remaining + C - 1) // C  # 필요한 부감독관 수: 올림 처리

# 결과 출력
print(result)

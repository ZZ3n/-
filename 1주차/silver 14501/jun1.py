# 백준 14501번 문제: 퇴사
# 문제 링크: https://velog.io/@re_bottle/%EB%B0%B1%EC%A4%80-%EC%82%BC%EC%84%B1-SW-%EC%97%AD%EB%9F%89-%ED%85%8C%EC%8A%A4%ED%8A%B8-%EA%B8%B0%EC%B6%9C-%EB%AC%B8%EC%A0%9C-14501%EB%B2%88-%ED%87%B4%EC%82%AC-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython
import sys

N = int(input())  # 상담 가능한 날짜 수
T = []  # 각 상담을 완료하는데 걸리는 기간
P = []  # 각 상담을 했을 때 받을 수 있는 금액
    
for _ in range(N):
    t, p = map(int, input().split())  # 기간과 금액 입력 받기
    T.append(t)
    P.append(p)
    
DP = [0] * (N+1)  # DP를 이용하여 각 날짜별 최대 수익 계산
    
for i in range(1, N+1):
    for j in range(1, i+1):
        if j + T[j-1] - 1 <= i:  # 상담이 퇴사 전에 끝나는 경우만 고려
            DP[i] = max(DP[i], DP[j-1] + P[j-1])  # 현재까지의 최대 수익 갱신
    
result = max(DP)  # 모든 날짜를 고려했을 때의 최대 수익

print(result)  # 최대 수익 출력

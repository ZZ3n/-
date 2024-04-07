# 백준 14889번 문제: 스타트와 링크
# 설명 링크: https://velog.io/@re_bottle/%EB%B0%B1%EC%A4%80-%EC%82%BC%EC%84%B1-SW-%EC%97%AD%EB%9F%89-%ED%85%8C%EC%8A%A4%ED%8A%B8-%EA%B8%B0%EC%B6%9C-%EB%AC%B8%EC%A0%9C-14889%EB%B2%88-%EC%8A%A4%ED%83%80%ED%8A%B8%EC%99%80-%EB%A7%81%ED%81%AC-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython
import sys
input = sys.stdin.readline  # 표준 입력 속도 향상

# 두 팀의 능력치 차이 계산 함수
def cal_diff(start_team, link_team):
    # 스타트 팀의 능력치 합계 계산
    start_power = sum([S[i][j] for i in start_team for j in start_team])
    # 링크 팀의 능력치 합계 계산
    link_power = sum([S[i][j] for i in link_team for j in link_team])
    # 두 팀의 능력치 차이의 절대값 반환
    return abs(start_power - link_power)

# 백트래킹을 이용한 팀 분배 함수
def backtrack(index, team):
    global min_diff  # 최소 능력치 차이를 갱신하기 위한 글로벌 변수
    if len(team) == n // 2:  # 팀 분배가 완료된 경우
        start_team = team  # 스타트 팀
        link_team = [x for x in range(n) if x not in start_team]  # 나머지 인원으로 링크 팀 구성
        diff = cal_diff(start_team, link_team)  # 두 팀의 능력치 차이 계산
        min_diff = min(min_diff, diff)  # 최소 능력치 차이 갱신
        return 
    for i in range(index, n):  # 가능한 모든 팀원 조합 탐색
        if i not in team:  # 중복 방지 조건
            team.append(i)  # 현재 인덱스의 선수를 팀에 추가
            backtrack(i +1, team)  # 다음 선수 탐색을 위해 재귀 호출
            team.pop()  # 백트래킹을 위한 현재 선수 제거

n = int(input())  # 참가 인원 수 입력
S = [list(map(int, input().split())) for _ in range(n)]  # 능력치 표 입력

min_diff = float('inf')  # 최소 능력치 차이를 저장할 변수 초기화

backtrack(0, [])  # 백트래킹 시작

print(min_diff)  # 계산된 최소 능력치 차이 출력

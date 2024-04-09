from itertools import combinations

S = []
N = int(input())
for i in range(N) :
  S_row = list(map(int, input().split()))
  S.append(S_row)


# 팀 능력치를 계산하는 함수
def team_ability(team, S):
  ability = 0
  for i in team :
    for j in team :
      ability += S[i][j]
  return ability


# 최소 능력치 차이를 계산하는 함수
def min_ability_difference(N, S):
  players = range(N) # 0 ~ N-1
  min_diff = float('inf')

  for team in combinations(players, N // 2):
    start_team = team
    link_team = tuple(set(players) - set(team))

    start_ability = team_ability(start_team, S)
    link_ability = team_ability(link_team, S)

    diff = abs(start_ability - link_ability) # 절댓값

    if diff < min_diff:
      min_diff = diff

  return min_diff

print(min_ability_difference(N, S))

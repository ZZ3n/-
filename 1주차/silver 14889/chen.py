"""
6명
d1   1
d2   2       3       4       5   6
d3   3 4 5 6 4 5 6   5 6     6   X
d4

6C3 / 2 = 10가지
남은 선택이 팀을 만들 수 없음 -> 중간 return
"""


def makeChoice(N, depth, arr: list, ret) -> None:
    if depth >= (N / 2):
        ret.append(arr)
        return
    for i in range(arr[-1] + 1, N + 1):
        if N - i < 0:
            break
        temp = arr.copy()
        temp.append(i)
        makeChoice(N, depth + 1, temp, ret)


def getTeamScoreDiff(M, team_roaster):
    opposite_team = [i + 1 for i in range(len(M)) if (i + 1 not in team_roaster)]
    return abs(getTeamScore(M, team_roaster) - getTeamScore(M, opposite_team))


def getTeamScore(M, team_roaster: list):
    _sum = 0
    for a in team_roaster:
        for b in team_roaster:
            if b < a:
                continue
            _sum = _sum + getV(M, a, b) + getV(M, b, a)
    return _sum


def getV(M, row, col):
    return M[row - 1][col - 1]


N = int(input())
M = [[] for i in range(N)]
for i in range(N):
    M[i] = list(map(int, input().split()))
numbers = [i + 1 for i in range(N)]

teams = []
makeChoice(N, 1, [1], teams)

result = []
for t in teams:
    result.append(getTeamScoreDiff(M, t))

print(min(result))

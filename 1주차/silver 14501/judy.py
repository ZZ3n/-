# 다이나믹 프로그래밍

n = int(input())
tasks = []
for i in range(n) :
    a, b = map(int, input().split())
    tasks.append([a, b])

# (작업의 시작일, 작업의 종료일, 작업으로 얻는 이익)
tasks_with_days = sorted([(i, i + tasks[i][0], tasks[i][1]) for i in range(n)], key=lambda x: x[0])

max_value = 0
dp = [0] * (n + 1)

for day in range(1, n + 1) :
    # day일까지 고려했을 때 얻을 수 있는 최대 이익
    dp[day] = dp[day - 1]
    for start_day, end_day, value in tasks_with_days :
        if end_day <= day :
            dp[day] = max(dp[day], dp[start_day] + value)

max_value = dp[n]
print(max_value)
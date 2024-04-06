def reject_interview(arr: list):
    new_arr = []
    for e in arr:
        if max(e['d']) < len(arr):
            new_arr.append(e)
    return new_arr


def they_has_overlap(a: list, b: list):
    for i in a:
        if i in b:
            return True
    return False


N = int(input())
arr = []
result = [{"i": j, "d": [], "v": 0} for j in range(N)]

for i in range(N):
    days, money = map(int, input().split())
    tempTuple = {"i": i, "d": [d for d in range(i, i + days)], "v": money}
    result[i] = tempTuple.copy()
    arr.append(tempTuple.copy())
arr = reject_interview(arr)
arr = sorted(arr, key=lambda item: item['v'], reverse=True)
result = reject_interview(result)

# print("###given schedules###")
# for i in arr:
#     print(i)


# print("### empty schedules ###")
# for i in result:
#     print(i)

for schedule in result:
    for elem in arr:
        if they_has_overlap(elem['d'], schedule['d']):
            continue
        else:
            schedule['d'] = schedule['d'] + elem['d']
            # schedule['d'].extend(elem['d']) // 이거 질문하기
            schedule['v'] = schedule['v'] + elem['v']

# print("### result schedules ###")
# for schedule in result:
#     print(schedule)

max_value = 0
for schedule in result:
    if schedule['v'] > max_value:
        max_value = schedule['v']

print(max_value)


"""
좀 억지로 푼 느낌
반례를 찾지 못해서 찾아봄.
1. 역순으로 그냥 더하기 -> 안됨
2. 테이블형식으로 더하기 -> 안됨
 -> 안된 이유는 shallow-copy 되서 -> 왜인지 모름.
3. 우선순위 두고, 테이블 형식으로 다 더하기 -> 됨.
"""
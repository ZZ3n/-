"""
특징 - 그래프가 정해져 있는 탐색 문제.
정답을 구하는데 특정한 수식이 없거나, 없다고 판단됨.
1안. DFS
2안. BFS
"""


def divide(a, b):
    is_negtive = True if a < 0 else False
    if is_negtive:
        k = -a // b
        return int(-k)
    return a // b


def has(operator: str, op_cnt_dict):
    return op_cnt_dict[operator] > 0


def operate(operator: str, op_cnt_dict: dict):
    temp = op_cnt_dict.copy()
    temp[operator] = temp[operator] - 1
    return temp


def dfs(numbers, op_cnt_dict, sum_, now):
    min_arr = []
    max_arr = []
    if now == 0:
        return dfs(numbers, op_cnt_dict, sum_=numbers[now], now=now + 1)
    if now == len(numbers):
        return sum_, sum_

    if has("plus", op_cnt_dict):
        temp_min, temp_max = dfs(numbers, operate("plus", op_cnt_dict),
                                 sum_=sum_ + numbers[now], now=now + 1)
        min_arr.append(temp_min)
        max_arr.append(temp_max)
    if has("minus", op_cnt_dict):
        temp_min, temp_max = dfs(numbers, operate("minus", op_cnt_dict),
                                 sum_=sum_ - numbers[now], now=now + 1)
        min_arr.append(temp_min)
        max_arr.append(temp_max)
    if has("multi", op_cnt_dict):
        temp_min, temp_max = dfs(numbers, operate("multi", op_cnt_dict),
                                 sum_=sum_ * numbers[now], now=now + 1)
        min_arr.append(temp_min)
        max_arr.append(temp_max)
    if has("div", op_cnt_dict):
        temp_min, temp_max = dfs(numbers, operate("div", op_cnt_dict),
                                 sum_=divide(sum_, numbers[now]), now=now + 1)
        min_arr.append(temp_min)
        max_arr.append(temp_max)
    return min(min_arr), max(max_arr)


N = int(input())
numbers = list(map(int, input().split()))
plus_cnt, minus_cnt, multi_cnt, divide_cnt = map(int, input().split())

op_cnt_dict = {"plus": plus_cnt, "minus": minus_cnt, "multi": multi_cnt, "div": divide_cnt}

result_min, result_max = dfs(numbers, op_cnt_dict, 0, 0)

print(result_max)
print(result_min)

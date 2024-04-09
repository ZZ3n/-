from itertools import permutations

n = int(input())
numbers = list(map(int, input().split()))
operators_count = list(map(int, input().split()))

operators = ["+"] * operators_count[0] + ["-"] * operators_count[1] + ["*"] * operators_count[2] + ["/"] * operators_count[3]

# 계산식 순열
operator_permutations = set(permutations(operators, len(operators)))

max_result = float('-inf')
min_result = float('inf')

def calculate(nums, ops) :
  result = nums[0]
  for i, op in enumerate(ops) :
    if op == "+" :
      result += nums[i + 1]
    elif op == "-" :
      result -= nums[i + 1]
    elif op == "*" :
      result *= nums[i + 1]
    elif op == "/" :
      if result < 0 :
        result = -(-result // nums[i + 1])
      else:
        result //= nums[i + 1]
  return result

for ops in operator_permutations :
  current_result = calculate(numbers, ops)
  max_result = max(max_result, current_result)
  min_result = min(min_result, current_result)

print(max_result, "\n", min_result, sep="")

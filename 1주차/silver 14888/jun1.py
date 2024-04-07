# 백준 14888번 문제: 연산자 끼워넣기
# 설명 링크: https://velog.io/@re_bottle/%EB%B0%B1%EC%A4%80-%EC%82%BC%EC%84%B1-SW-%EC%97%AD%EB%9F%89-%ED%85%8C%EC%8A%A4%ED%8A%B8-%EA%B8%B0%EC%B6%9C-%EB%AC%B8%EC%A0%9C-14888%EB%B2%88-%EC%97%B0%EC%82%B0%EC%9E%90-%EB%81%BC%EC%9B%8C%EB%84%A3%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython
import sys

# 연산 수행 함수
def calculate(op, a, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        # 음수 나눗셈의 경우 올림 처리
        if a * b < 0 and a % b != 0:
            return a // b + 1
        return a // b

# 백트래킹을 이용한 모든 경우의 수 탐색
def backtrack(index, current_result):
    global addition_count, subtraction_count, multiplication_count, division_count

    if index == n:  # 모든 숫자를 사용한 경우
        results.add(current_result)  # 최종 결과를 결과 집합에 추가
        return
    
    # 덧셈 연산자가 남아있는 경우
    if addition_count > 0:
        addition_count -= 1
        backtrack(index + 1, calculate('+', current_result, input_arr[index]))
        addition_count += 1
    
    # 뺄셈 연산자가 남아있는 경우
    if subtraction_count > 0:
        subtraction_count -= 1
        backtrack(index + 1, calculate('-', current_result, input_arr[index]))
        subtraction_count += 1
    
    # 곱셈 연산자가 남아있는 경우
    if multiplication_count > 0:
        multiplication_count -= 1
        backtrack(index + 1, calculate('*', current_result, input_arr[index]))
        multiplication_count += 1
    
    # 나눗셈 연산자가 남아있는 경우
    if division_count > 0:
        division_count -= 1
        backtrack(index + 1, calculate('/', current_result, input_arr[index]))
        division_count += 1    
    
input = sys.stdin.readline  # 표준 입력 속도 향상

n = int(input())  # 숫자의 개수 입력
input_arr = list(map(int, input().strip().split()))  # 숫자들 입력

# 각 연산자의 개수 입력
addition_count, subtraction_count, multiplication_count, division_count = map(int, input().strip().split())

results = set()  # 가능한 모든 결과를 저장할 집합

backtrack(1, input_arr[0])  # 백트래킹 시작
print(max(results))  # 가능한 결과들 중 최댓값 출력
print(min(results))  # 가능한 결과들 중 최솟값 출력

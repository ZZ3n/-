"""
N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

A_set = set(A)
result = 0
for i in A_set :
    if i > B :
        left = (i - B) // C
        ass = (i - B) % C
        if ass == 0 :
            result += (left + 1) * A.count(i)
        else :
            result += (left + 2) * A.count(i)
    else :
        result += A.count(i)
print(result)

"""
import sys
input = sys.stdin.read # 대량 데이터 빠르게 입력
from collections import Counter

data = input().split()
N = int(data[0])
A = list(map(int, data[1:N+1]))
B, C = map(int, data[N+1:])

frequency = Counter(A)  # A 리스트의 각 원소 빈도 계산

result = 0
for i, count in frequency.items():
    if i > B:
        # i - B > 0 일 때
        left = (i - B) // C
        if (i - B) % C == 0:
            result += (left + 1) * count
        else:
            result += (left + 2) * count
    else:
        # i <= B 일 때, 감독관 1명 필요
        result += count

print(result)

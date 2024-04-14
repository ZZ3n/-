N = int(input())
arr_A = map(int, input().split())
main_director, sub_director = map(int, input().split())
result = 0

for A in arr_A:
    sub_direc_cnt = 0
    remain = A - main_director
    if remain > 0:
        sub_direc_cnt = remain // sub_director
        if remain % sub_director != 0:
            sub_direc_cnt += 1
    result += 1 + sub_direc_cnt

print(result)

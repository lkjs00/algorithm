N = int(input())

arr = [list(map(str, input())) for _ in range(N)]

def find(Arr):
    max_val = 0
    for i in range(N):
        tmp_val = Arr[i][0]
        tmp_cnt = 1
        for j in range(1, N):
            if tmp_val == Arr[i][j]:
                tmp_cnt += 1
            else:
                tmp_val = Arr[i][j]
                tmp_cnt = 1
            if max_val < tmp_cnt:
                max_val = tmp_cnt

    for i in range(N):
        tmp_val = Arr[0][i]
        tmp_cnt = 1
        for j in range(1, N):
            if tmp_val == Arr[j][i]:
                tmp_cnt += 1
            else:
                tmp_val = Arr[j][i]
                tmp_cnt = 1
            if max_val < tmp_cnt:
                max_val = tmp_cnt
    return max_val

answer = 0
for i in range(N):
    for j in range(N):
        tmp_arr = arr
        if i + 1 < N:
            tmp_arr[i][j], tmp_arr[i + 1][j] = tmp_arr[i + 1][j], tmp_arr[i][j]
            tmp = find(tmp_arr)
            tmp_arr[i][j], tmp_arr[i + 1][j] = tmp_arr[i + 1][j], tmp_arr[i][j]
            if answer < tmp:
                answer = tmp
        tmp_arr = arr
        if j + 1 < N:
            tmp_arr[i][j], tmp_arr[i][j + 1] = tmp_arr[i][j + 1], tmp_arr[i][j]
            tmp = find(tmp_arr)
            tmp_arr[i][j], tmp_arr[i][j + 1] = tmp_arr[i][j + 1], tmp_arr[i][j]
            if answer < tmp:
                answer = tmp
print(answer)
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
min_val = 999999
def find(fuel, way, cnt, tmp):
    global min_val
    if cnt == N - 1:
        if min_val > fuel:
            min_val = fuel
        return
    if way == 0:
        find(fuel + arr[cnt + 1][tmp], 1, cnt + 1, tmp)
        if tmp + 1 < M:
            find(fuel + arr[cnt + 1][tmp + 1], 2, cnt + 1, tmp + 1)
    elif way == 1:
        if tmp - 1 >= 0:
            find(fuel + arr[cnt + 1][tmp - 1], 0, cnt + 1, tmp - 1)
        if tmp + 1 < M:
            find(fuel + arr[cnt + 1][tmp + 1], 2, cnt + 1, tmp + 1)
    elif way == 2:
        find(fuel + arr[cnt + 1][tmp], 1, cnt + 1, tmp)
        if tmp - 1 >= 0:
            find(fuel + arr[cnt + 1][tmp - 1], 0, cnt + 1, tmp - 1)
    elif way == 3:
        find(fuel + arr[cnt + 1][tmp], 1, cnt + 1, tmp)
        if tmp - 1 >= 0:
            find(fuel + arr[cnt + 1][tmp - 1], 0, cnt + 1, tmp - 1)
        if tmp + 1 < M:
            find(fuel + arr[cnt + 1][tmp + 1], 2, cnt + 1, tmp + 1)

for i in range(M):
    find(arr[0][i], 3, 0, i)


print(min_val)
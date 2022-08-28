N = int(input())
arr = list(list(input()) for _ in range(N))

dx = [0, 1]
dy = [1, 0]

def find():
    max_val = 1
    for i in range(N):
        for j in range(N):
            for k in range(2):
                cnt = 1
                n = 1
                while True:
                    ddx = i + (n * dx[k])
                    ddy = j + (n * dy[k])
                    if 0 <= ddx < N and 0 <= ddy < N:
                        if arr[i][j] == arr[ddx][ddy]:
                            cnt += 1
                        else:
                            break
                    else:
                        break
                    n += 1
                if cnt > max_val:
                    max_val = cnt
                if cnt == N:
                    return N
    return max_val

result = 0
for i in range(N):
    for j in range(N):
        for k in range(2):
            ddx = i + dx[k]
            ddy = j + dy[k]
            if 0 <= ddx < N and 0 <= ddy < N:
                arr[i][j], arr[ddx][ddy] = arr[ddx][ddy], arr[i][j]
                max_val = find()
                if max_val > result:
                    result = max_val
                arr[i][j], arr[ddx][ddy] = arr[ddx][ddy], arr[i][j]
                if result == N:
                    break

print(result)
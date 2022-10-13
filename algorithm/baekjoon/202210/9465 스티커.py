T = int(input())

for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]

    DP = [[0, 0] for _ in range(N)]

    DP[0][0] = arr[0][0]

    for i in range(N):
        if DP[i][0] != 0 and i + 2 < N:
            if arr[1 - DP[i][1]][i + 1] + arr[DP[i][1]][i + 2] > arr[1 - DP[i][1]][i + 2]:
                DP[i + 1][0] = DP[i][0] + arr[1 - DP[i][1]][i + 1]
                DP[i + 1][1] = 1 - DP[i][1]
            else:
                DP[i + 2][0] = DP[i][0] + arr[1 - DP[i][1]][i + 2]
                DP[i + 2][1] = DP[i][1]
    max_val = 0
    for i in DP:
        if max_val < i[0]:
            max_val = i[0]

    DP = [[0, 0] for _ in range(N)]

    DP[0][0] = arr[0][1]
    DP[0][1] = 1

    for i in range(N):
        if DP[i][0] != 0 and i + 2 < N:
            if arr[1 - DP[i][1]][i + 1] + arr[DP[i][1]][i + 2] > arr[1 - DP[i][1]][i + 2]:
                DP[i + 1][0] = DP[i][0] + arr[1 - DP[i][1]][i + 1]
                DP[i + 1][1] = 1 - DP[i][1]
            else:
                DP[i + 2][0] = DP[i][0] + arr[1 - DP[i][1]][i + 2]
                DP[i + 2][1] = DP[i][1]
    for i in DP:
        if max_val < i[0]:
            max_val = i[0]

    print(max_val)
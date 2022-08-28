N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

dp = [[0] * N for _ in range(N)]

dp[0][0] = 1
for i in range(N):
    for j in range(N):
        if dp[i][j] != 0:
            if i == N - 1 and j == N - 1: continue
            if i + arr[i][j] < N: dp[i + arr[i][j]][j] += dp[i][j]
            if j + arr[i][j] < N: dp[i][j + arr[i][j]] += dp[i][j]

print(dp[N - 1][N - 1])
N = int(input())
dp = [1] * 10000
for i in range(9998):
    dp[i + 2] += dp[i]
for i in range(9997):
    dp[i + 3] += dp[i]
dp.pop(0)

for _ in range(N):
    print(dp[int(input()) - 1])
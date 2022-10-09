N = int(input())
work = []
for _ in range(N):
    T, P = map(int, input().split())
    work.append((T, P))

DP = [0] * (N + 1)

for i in range(N):
    if i + work[i][0] < N + 1:
        if DP[i] + work[i][1] > DP[i + work[i][0]]:
            DP[i + work[i][0]] = DP[i] + work[i][1]
        else:


print(DP)
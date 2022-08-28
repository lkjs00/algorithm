N = int(input())
arr = list(map(int, input().split()))

cnt = N

for i in range(N):
    if arr[i] == 1:
        cnt -= 1
    else:
        for j in range(2, arr[i] - 1):
            if arr[i] % j == 0:
                cnt -= 1
                break

print(cnt)
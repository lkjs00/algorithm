H, W, X, Y = map(int, input().split())
arr = []
for _ in range(H + X):
    arr.append(list(map(int, input().split())))

arr1 = [[0] * (W + Y) for _ in range(H + X)]

for i in range(H):
    for j in range(W):
        arr1[i][j] += 1
for i in range(X, H + X):
    for j in range(Y, W + Y):
        arr1[i][j] += 1

answer = [[0] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if arr1[i][j] == 1:
            answer[i][j] = arr[i][j]
        elif arr1[i][j] == 2:
            answer[i][j] = arr[i][j] - arr[i - X][j - Y]

for i in range(len(answer)):
    for j in answer[i]:
        print(j, end=' ')
    if i != len(answer) - 1:
        print()
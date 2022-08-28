def solution(width, height, diagonals):
    answer = 0
    arr = [[0] * (width + 1) for _ in range(height + 1)]
    arr[0][0] = 1
    for i in range(height + 1):
        if i == 0:
            for j in range(1, width + 1):
                arr[0][j] = arr[0][j - 1]
                if (i == diagonals[0][1] - 1 and j == diagonals[0][0]) or (i == diagonals[0][1] and j == diagonals[0][0] - 1):
                    arr[i][j] *= 2
        else:
            for j in range(width + 1):
                if j == 0:
                    arr[i][j] = arr[i - 1][j]
                    if (i == diagonals[0][1] - 1 and j == diagonals[0][0]) or (i == diagonals[0][1] and j == diagonals[0][0] - 1):
                        arr[i][j] *= 2
                else:
                    arr[i][j] = arr[i - 1][j] + arr[i][j - 1]
                    if (i == diagonals[0][1] - 1 and j == diagonals[0][0]) or (i == diagonals[0][1] and j == diagonals[0][0] - 1):
                        arr[i][j] *= 2  
    return arr[height][width] % 10000019

print(solution(2, 2, [[1, 1], [2, 2]]))
print(solution(51, 37, [[17, 19]]))
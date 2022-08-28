def solution(n, clockwise):
    answer = [[0] * n for _ in range(n)]

    tmp_x = 0
    tmp_y = 0
    tmp_value = 0
    cnt = 1
    while True:
        if tmp_x > (n // 2):break

        if clockwise:
            for i in range(n - cnt):
                answer[tmp_x][tmp_y + i] = tmp_value + i + 1
            for i in range(n - cnt):
                answer[tmp_x + i][n - 1 - tmp_y] = tmp_value + i + 1
            for i in range(n - cnt):
                answer[n - 1 - tmp_x][n - 1 - tmp_y - i] = tmp_value + i + 1
            for i in range(n - cnt):
                answer[n - 1 - tmp_x - i][tmp_y] = tmp_value + i + 1
        else:
            for i in range(n - cnt):
                answer[tmp_x + i][tmp_y] = tmp_value + i + 1
            for i in range(n - cnt):
                answer[n - 1 - tmp_x][tmp_y + i] = tmp_value + i + 1
            for i in range(n - cnt):
                answer[n - 1 - tmp_x - i][n - 1 - tmp_y] = tmp_value + i + 1
            for i in range(n - cnt):
                answer[tmp_x][n - 1 - tmp_y - i] = tmp_value + i + 1
                
        
        tmp_value += (n - cnt)
        cnt += 2
        tmp_x += 1
        tmp_y += 1
    
    if n % 2:
        answer[tmp_x - 1][tmp_y - 1] = tmp_value + 1
    return answer

print(solution(5, True))
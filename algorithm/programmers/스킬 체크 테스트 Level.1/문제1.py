def solution(n):
    answer = 0
    tmp = ''
    while True:
        if n < 3:
            tmp += str(n)
            break
        tmp += str(n % 3)
        n = n // 3

    for i in range(len(tmp) - 1, -1, -1):
        answer += int(tmp[i]) * (3 ** (len(tmp) - i - 1))
    return answer

solution(45)
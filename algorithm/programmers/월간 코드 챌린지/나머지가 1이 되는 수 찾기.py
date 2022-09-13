def solution(n):
    answer = 1
    while True:
        answer += 1
        if n % answer == 1:
            break
    return answer
def solution(seoul):
    answer = '김서방은 '
    for idx in range(len(seoul)):
        if seoul[idx] == 'Kim':
            answer += str(idx) + '에 있다'
    return answer
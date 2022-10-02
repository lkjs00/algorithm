def solution(array):
    answer = 0
    for element in array:
        for i in str(element):
            if i == '7':
                answer += 1
    return answer
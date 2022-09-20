def solution(a, b):
    answer = ''
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']

    tmp_sum = 0
    for i in range(a):
        tmp_sum += month[i]
    tmp_sum += b

    return day[(tmp_sum % 7) - 1]

print(solution(1, 1))
print(solution(2, 1))
print(solution(3, 1))
print(solution(4, 1))
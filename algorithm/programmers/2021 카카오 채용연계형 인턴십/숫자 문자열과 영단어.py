def solution(s):
    answer = ''
    tmp_num = 0
    # 숫자 48-57
    for i in range(len(s)):
        if tmp_num != 0:
            tmp_num -= 1
            continue

        if 48 <= ord(s[i]) <= 57:
            answer += s[i]
        if i == len(s) - 1:
            continue

        if s[i] == 'z':
            answer += '0'
            tmp_num = 3
        elif s[i] == 'o':
            answer += '1'
            tmp_num = 2
        elif s[i] == 't':
            if s[i + 1] == 'w':
                answer += '2'
                tmp_num = 2
            else:
                answer += '3'
                tmp_num = 4
        elif s[i] == 'f':
            if s[i + 1] == 'o':
                answer += '4'
                tmp_num = 3
            else:
                answer += '5'
                tmp_num = 3
        elif s[i] == 's':
            if s[i + 1] == 'i':
                answer += '6'
                tmp_num = 2
            else:
                answer += '7'
                tmp_num = 4
        elif s[i] == 'e':
            answer += '8'
            tmp_num = 4
        elif s[i] == 'n':
            answer += '9'
            tmp_num = 3
    return int(answer)

print(solution("one4seveneight"))
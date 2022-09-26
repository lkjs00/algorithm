def solution(s):
    answer = ''
    sentence = list(s.split(' '))

    for word in sentence:
        for idx in range(len(word)):
            if idx % 2:
                answer += word[idx].lower()
            else:
                answer += word[idx].upper()
        answer += ' '
    return answer[:-1]
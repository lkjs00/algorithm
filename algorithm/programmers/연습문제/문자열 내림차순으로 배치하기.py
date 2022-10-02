def solution(s):
    answer = ''
    tmp_arr = []
    for element in s:
        tmp_arr.append(ord(element))
    tmp_arr.sort(reverse=True)
    for tmp in tmp_arr:
        answer += chr(tmp)
    return answer
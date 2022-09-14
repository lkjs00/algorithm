def solution(s):
    answer = ''
    arr = list(map(int, s.split()))
    answer += min(arr) + ' ' + max(arr)
    return answer
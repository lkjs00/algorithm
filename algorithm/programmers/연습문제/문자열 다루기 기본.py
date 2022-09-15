def solution(s):

    if len(s) == 4 or len(s) == 6: pass
    else: return False

    for i in s:
        if 48 <= ord(i) <= 57:
            pass
        else:
            return False
    return True

solution("1234")
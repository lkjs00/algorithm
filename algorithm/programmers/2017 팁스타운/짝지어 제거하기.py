def solution(s):
    answer = -1
    stack = []
    for element in s:
        if len(stack) == 0:
            stack.append(element)
        else:
            if element == stack[-1]:
                stack.pop()
            else:
                stack.append(element)
    if len(stack) == 0:answer = 1
    else:answer = 0
    return answer

print(solution("baabaa"))
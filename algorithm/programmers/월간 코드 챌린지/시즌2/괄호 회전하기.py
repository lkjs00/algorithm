def solution(s):
    answer = 0
    def find(words):
        stack = []
        for word in words:
            if len(stack) == 0:
                if word == ')' or word == ']' or word == '}':
                    return False
                stack.append(word)
                continue
            if word == '(' or word == '[' or word == '{':
                stack.append(word)
            elif word == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif word == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            elif word == '}':
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        if len(stack) > 0:
            return False
        else:
            return True

    for i in range(len(s)):
        if find(s):
            answer += 1
        s = s[1:] + s[0]
    return answer

print(solution("[](){}"))
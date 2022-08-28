def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for i in range(len(prices)):
        if len(stack) == 0:
            stack.append((prices[i], i))
        else:
            for j in range(len(stack) - 1, -1, -1):
                if stack[j][0] <= prices[i]:
                    stack.append((prices[i], i))
                    break
                else:
                    component = stack.pop()
                    answer[component[1]] = j - component[1]
    return answer

solution([1, 2, 3, 2, 3])
def solution(queue1, queue2):
    answer = 0
    N = sum(queue1) + sum(queue2)
    if N % 2: return -1

    while True:
        if sum(queue1) == sum(queue2):
            break
        elif sum(queue1) > sum(queue2):
            queue2.append(queue1.pop(0))
            answer += 1
        else:
            queue1.append(queue2.pop(0))
            answer += 1
    return answer

# 2
print(solution([3, 2, 7, 2], [4, 6, 5, 1]))

# 7
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
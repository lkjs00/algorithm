def solution(numbers):
    answer = []
    N = len(numbers)
    for i in range(N):
        for j in range(i + 1, N):
            if numbers[i] + numbers[j] in answer:
                pass
            else:
                answer.append(numbers[i] + numbers[j])
    answer.sort()
    return answer
def solution(numbers, target):
    answer = 0

    def find(idx, tmp_sum):
        nonlocal answer
        if idx == len(numbers):
            if tmp_sum == target:
                answer += 1
            return

        find(idx + 1, tmp_sum + numbers[idx])

        find(idx + 1, tmp_sum - numbers[idx])

    find(0, 0)
    return answer

solution([1, 1, 1, 1, 1], 3)
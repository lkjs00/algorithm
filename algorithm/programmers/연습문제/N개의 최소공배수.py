def solution(arr):
    answer = 0
    arr.sort()
    answer = arr.pop(0)
    for _ in range(len(arr)):
        tmp_num = arr.pop()
        tmp = 1
        for i in range(min(answer, tmp_num), 0, -1):
            if tmp_num % i == 0 and answer % i == 0:
                tmp = i
                break
        answer = int(tmp * (tmp_num / tmp) * (answer / tmp))
    return answer

print(solution([1, 2, 3, 4, 5, 6]))
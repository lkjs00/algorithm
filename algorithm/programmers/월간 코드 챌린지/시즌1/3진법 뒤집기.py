def solution(n):
    answer = 0
    arr = []
    while n >= 3:
        a = n % 3
        n = n // 3
        arr.append(a)
    arr.append(n)

    for i in range(len(arr)):
        answer += arr[i] * (3 ** (len(arr) - i - 1))

    return answer

solution(45)
solution(125)
def solution(n):
    answer = 0
    arr = [0] * 2000

    arr[0] = 1
    arr[1] = 2
    for i in range(2, 2000):
        arr[i] = arr[i - 1] + arr[i - 2]


    return arr[n - 1] % 1234567

solution(4)
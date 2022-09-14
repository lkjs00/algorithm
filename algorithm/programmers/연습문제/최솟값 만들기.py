def solution(A,B):
    answer = 0
    A.sort(reverse=True)
    B.sort()
    for _ in range(len(A)):
        answer += A.pop() * B.pop()
    return answer

solution([1, 4, 2], [5, 4, 4])
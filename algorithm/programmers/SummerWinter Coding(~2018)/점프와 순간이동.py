def solution(n):
    ans = 0

    while n > 1:
        if n % 2:
            n -= 1
            ans += 1
        else:
            n = n / 2

    return ans + 1

print(solution(5000))
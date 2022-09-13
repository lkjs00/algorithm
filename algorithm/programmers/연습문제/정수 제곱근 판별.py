import math
def solution(n):
    for i in range(1, int(math.sqrt(n)) + 1):
        if i * i == n:
            return (i + 1) ** 2
    return -1
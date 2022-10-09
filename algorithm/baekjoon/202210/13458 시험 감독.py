N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
answer = 0

for i in A:
    i -= B
    answer += 1

    if i <= 0:
        continue
    else:
        if i % C == 0:
            answer += (i // C)
        else:
            answer += (i // C) + 1
print(answer)
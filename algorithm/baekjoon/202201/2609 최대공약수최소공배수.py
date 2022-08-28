A, B = map(int, input().split())

for i in range(1, min(A, B) + 1):
    if A % i == 0 and B % i == 0:
        max_val = i

n = 1
while True:
    if (max(A, B) * n) % min(A, B) == 0:
        min_val = max(A, B) * n
        break
    else:
        n += 1

print(max_val)
print(min_val)
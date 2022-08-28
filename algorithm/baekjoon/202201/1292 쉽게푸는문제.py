arr = []

for i in range(1, 200):
    for j in range(i):
        arr.append(i)
result = 0

A, B = map(int, input().split())

for i in range(A - 1, B):
    result += arr[i]

print(result)
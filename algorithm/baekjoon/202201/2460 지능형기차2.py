arr = []
for _ in range(10):
    arr.append(list(map(int, input().split())))

temp = 0
result = 0
for i in range(10):
    temp -= arr[i][0]
    if temp > result:
        result = temp
    temp += arr[i][1]
    if temp > result:
        result = temp
print(result)
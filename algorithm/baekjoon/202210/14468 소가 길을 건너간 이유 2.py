arr = list(map(str, input()))

arr2 = {}
for i in range(len(arr)):
    if arr[i] not in arr2:
        arr2[arr[i]] = [i]
    else:
        if arr2[arr[i]][0] + 1 == i:
            arr2.pop(arr[i])
        else:
            arr2[arr[i]].append(i)

answer = 0
for i in arr2:
    for j in arr2:
        if arr2[i][0] < arr2[j][1] and arr2[i][1] > arr2[j][0] and i != j:
            answer += 1
print(answer // 2)
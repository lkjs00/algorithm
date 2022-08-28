M = int(input())
N = int(input())

arr = []
for i in range(M, N + 1):
    if i == 1:
        pass
    elif i == 2:
        arr.append(i)
    else:
        cnt = 0
        for j in range(2, i):
            if i % j == 0:
                cnt += 1
        if cnt == 0:
            arr.append(i)

if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(arr[0])
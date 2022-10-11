N = int(input())
arr = [0] * 40
arr[0] = 1
for i in range(1, 40):
    arr[i] = arr[i - 1] + i + 1

for _ in range(N):
    X = int(input())
    flag = True
    for i in range(40):
        for j in range(40):
            for k in range(40):
                if arr[i] + arr[j] + arr[k] == X:
                    flag = False
                    print(1)
                    break
            if flag == False:
                break
        if flag == False:
            break
    if flag:
        print(0)
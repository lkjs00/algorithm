N = int(input())
arr = []

for i in range(N):
    tmp = list(map(int, input().split()))
    tmp.append(i+1)
    arr.append(tmp)

tmp = [0] * N

arr.sort(key=lambda x:len(x))

for i in arr:
    if len(i) == 3:
        tmp[i[-1] - 1] = i[0]
    else:
        tmp[i[-1] - 1] = i[0]
        _max = 0
        for j in range(1, len(i) - 2):
            if _max < tmp[i[j] - 1]:
                _max = tmp[i[j] - 1]
        tmp[i[-1] - 1] += _max

for i in tmp:
    print(i)
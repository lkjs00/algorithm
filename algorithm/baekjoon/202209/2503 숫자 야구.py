N = int(input())
arr = []
# for i in range(1, 10):
#     for j in range(10):
#         for k in range(10):
#             arr.append(int(str(i) + str(j) + str(k)))

for _ in range(N):
    num, strike, ball = map(int, input().split())
    num = str(num)
    if strike == 3:
        arr.append([int(num)])
    elif strike == 2:
        tmp = []
        for i in range(10):
            tmp.append(int(num[0:2] + str(i)))
            if i == 0:
                pass
            else:
                tmp.append(int(str(i) + num[1:3]))
        arr.append(tmp)
    elif strike == 1 and ball == 2:
        tmp = []
        tmp.append(int(num[0] + num[2] + num[1]))
        tmp.append(int(num[2] + num[1] + num[0]))
        tmp.append(int(num[1] + num[0] + num[2]))
        arr.append(tmp)
    elif strike == 1 and ball == 1:
        tmp = []
        for i in range(10):
    elif strike == 1 and ball == 0:

print(arr)

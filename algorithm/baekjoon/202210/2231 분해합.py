N = int(input())

flag = True
for i in range(N):
    tmp = i
    for j in str(i):
        tmp += int(j)
    if tmp == N:
        print(i)
        flag = False
        break
if flag:
    print(0)
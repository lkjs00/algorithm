N = int(input())
answer = []
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            tmp = str(i) + str(j) + str(k)
            answer.append(tmp)

for i in range(N):
    num, strike, ball = map(int, input().split())
    a, b, c = str(num)[0], str(num)[1], str(num)[2]

    for j in answer:
        d, e, f = j[0], j[1], j[2]
        


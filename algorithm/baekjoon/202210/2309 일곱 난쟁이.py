person = []
for _ in range(9):
    person.append(int(input()))

answer = []
for i in range(9):
    tmp = sum(person)
    for j in range(i + 1, 9):
        if tmp - person[i] - person[j] == 100:
            a, b = i, j
for i in range(9):
    if i != a and i != b:
        answer.append(person[i])
answer.sort()

for i in answer:
    print(i)
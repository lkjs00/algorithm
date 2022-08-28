N = int(input())
arr = list(map(int, input().split()))
operation = list(map(int, input().split()))

max = -1000000000
min = 1000000000

def find(idx, result):
    global max, min, operation
    if idx == N - 1:
        if result > max:
            max = result
        if result < min:
            min = result
        return
    else:
        for i in range(4):
            if i == 0 and operation[0] > 0:
                operation[0] -= 1
                if idx == 0:
                    find(idx + 1, result + arr[idx] + arr[idx + 1])
                else:
                    find(idx + 1, result + arr[idx + 1])
                operation[0] += 1
            elif i == 1 and operation[1] > 0:
                operation[1] -= 1
                if idx == 0:
                    find(idx + 1, result + arr[idx] - arr[idx + 1])
                else:
                    find(idx + 1, result - arr[idx + 1])
                operation[1] += 1
            elif i == 2 and operation[2] > 0:
                operation[2] -= 1
                if idx == 0:
                    find(idx + 1, result + (arr[idx] * arr[idx + 1]))
                else:
                    find(idx + 1, result * arr[idx + 1])
                operation[2] += 1
            elif i == 3 and operation[3] > 0:
                operation[3] -= 1
                if idx == 0:
                    if arr[idx] < 0:
                        find(idx + 1, result - (-arr[idx] // arr[idx + 1]))
                    else:
                        find(idx + 1, result + (arr[idx] // arr[idx + 1]))
                else:
                    if result < 0:
                        find(idx + 1, -(-result // arr[idx + 1]))
                    else:
                        find(idx + 1, result // arr[idx + 1])
                operation[3] += 1

find(0, 0)

print(max, min)
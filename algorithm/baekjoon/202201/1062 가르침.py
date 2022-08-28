N, K = map(int, input().split())
arr = []
for _ in range(N):
    word = input()
    word = word.replace('a', '')
    word = word.replace('n', '')
    word = word.replace('t', '')
    word = word.replace('i', '')
    word = word.replace('c', '')
    arr.append(word)

K -= 5

arr.sort(key=lambda x : len(x))

result = 0
for i in range(len(arr)):
    if len(arr[i]) == 0:
        result += 1
    elif len(arr[i]) > K or K <= 0:
        break
    elif 0 < K <= len(arr[i]):
        K -= len(arr[i])
        for j in range(len(arr[i]) - 1, -1, -1):
            word = arr[i][j]
            for k in range(len(arr)):
                arr[k] = arr[k].replace(word, '')
        result += 1
        
print(result)
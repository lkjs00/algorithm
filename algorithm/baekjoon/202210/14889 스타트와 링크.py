from itertools import combinations

N = int(input())
score = []
for _ in range(N):
    score.append(list(map(int, input().split())))

arr = range(N)
arr2 = combinations(arr, N // 2)

for i in arr2:
    print(i)
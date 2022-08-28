n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)
print(arr)
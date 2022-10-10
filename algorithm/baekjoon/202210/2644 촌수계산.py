n = int(input())
a, b = map(int, input().split())
m = int(input())
arr = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    x, y  = map(int, input().split())
    arr[x][y] = 1
    arr[y][x] = 1
print(arr)
visited = [False] * (n + 1)
result = []
def dfs(v, num):
  num += 1
  visited[v] = 1

  if v == b:
    result.append(num)

  for i in arr[v]:
    if not visited[i]:
      dfs(i, num)

dfs(a, 0)
print(result)


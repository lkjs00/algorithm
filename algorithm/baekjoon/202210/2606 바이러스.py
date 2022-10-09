N = int(input())

arr = [[0] * N for _ in range(N)]
for _ in range(int(input())):
    i, j = map(int, input().split())
    arr[i - 1][j - 1] = 1
    arr[j - 1][i - 1] = 1

stack = [0]
visited = [0] * N
visited[0] = 1
answer = 0
while stack:
    cur = stack.pop(0)
    for i in range(N):
        if arr[cur][i] == 1 and visited[i] == 0:
            stack.append(i)
            answer += 1
            visited[i] = 1

print(answer)
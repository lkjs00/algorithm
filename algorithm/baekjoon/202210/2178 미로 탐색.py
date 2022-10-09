N, M = map(int, input().split())
arr = []
visited = [[0] * M for _ in range(N)]

for _ in range(N):
    arr.append(list(map(int, input())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

stack = [(0, 0)]
visited[0][0] = 1
while stack:
    cur = stack.pop(0)
    for i in range(4):
        ddx = cur[0] + dx[i]
        ddy = cur[1] + dy[i]
        if 0 <= ddx < N and 0 <= ddy < M and visited[ddx][ddy] == 0 and arr[ddx][ddy] == 1:
            stack.append((ddx, ddy))
            visited[ddx][ddy] = visited[cur[0]][cur[1]] + 1



print(visited[N - 1][M - 1])
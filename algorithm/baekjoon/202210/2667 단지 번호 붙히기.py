def find(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    q = [(x, y)]
    visited[x][y] = 1
    cnt = 0
    while q:
        cur = q.pop(0)
        for i in range(4):
            ddx = cur[0] + dx[i]
            ddy = cur[1] + dy[i]
            if 0 <= ddx < N and 0 <= ddy < N and visited[ddx][ddy] == 0 and arr[ddx][ddy] == 1:
                q.append((ddx, ddy))
                visited[ddx][ddy] = visited[cur[0]][cur[1]] + 1
                cnt += 1
    return cnt + 1

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

answer_arr = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            answer = find(i, j)
            answer_arr.append(answer)

answer_arr.sort()
print(len(answer_arr))
for i in answer_arr:
    print(i)
N, M = map(int, input().split())
arr = []
for _ in range(M):
    arr.append(list(input()))

visited = [[0] * N for _ in range(M)]

we = 0
they = 0

def find(x, y):
    global we, they
    if visited[x][y] == 1: return
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    q = [(x,y)]
    visited[x][y] = 1
    if arr[x][y] == 'B': flag = True
    elif arr[x][y] == 'W': flag = False

    cnt = 1
    while q:
        cur = q.pop(0)
        for i in range(4):
            ddx = cur[0] + dx[i]
            ddy = cur[1] + dy[i]
            if 0 <= ddx < M and 0 <= ddy < N and visited[ddx][ddy] == 0 and arr[cur[0]][cur[1]] == arr[ddx][ddy]:
                q.append((ddx, ddy))
                visited[ddx][ddy] = 1
                cnt += 1
    if flag: we += (cnt * cnt)
    else: they += (cnt * cnt)

for i in range(M):
    for j in range(N):
        find(i, j)
print(they, we)
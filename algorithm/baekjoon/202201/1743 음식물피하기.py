N, M, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]
for _ in range(K):
    x, y = map(int, input().split())
    arr[x - 1][y - 1] = 1

result = 0

def find(x, y):
    if arr[x][y] == 0: return 0
    elif arr[x][y] == 1 and visited[x][y] == 1: return 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    stack = [(x, y)]
    cnt = 1
    visited[x][y] = 1
    while stack:
        cur = stack.pop(0)
        for i in range(4):
            ddx = cur[0] + dx[i]
            ddy = cur[1] + dy[i]
            if 0 <= ddx < N and 0 <= ddy < M and visited[ddx][ddy] == 0 and arr[ddx][ddy] == 1:
                stack.append((ddx, ddy))
                visited[ddx][ddy] = 1
                cnt += 1
    return cnt

for i in range(N):
    for j in range(M):
        cnt = find(i, j)
        if cnt > result: result = cnt
print(result)
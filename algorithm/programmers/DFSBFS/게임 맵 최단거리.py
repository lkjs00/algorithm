from collections import deque


def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])

    visited = [[0] * m for _ in range(n)]

    q = deque()
    q.append((0, 0))
    visited[0][0] = 1

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while q:
        cur = q.popleft()
        for i in range(4):
            ddx = dx[i] + cur[0]
            ddy = dy[i] + cur[1]
            if 0 <= ddx < n and 0 <= ddy < m and maps[ddx][ddy] == 1 and visited[ddx][ddy] == 0:
                q.append((ddx, ddy))
                visited[ddx][ddy] = visited[cur[0]][cur[1]] + 1
    if visited[n - 1][m - 1] == 0:
        answer = -1
    else:
        answer = visited[n - 1][m - 1]
    return answer
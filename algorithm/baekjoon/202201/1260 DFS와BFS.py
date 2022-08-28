N, M, V = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A][B] = 1
    graph[B][A] = 1

dfs = []
bfs = []

# 각 노드의 방문유무
visited = [0] * (N + 1)

# dfs 함수
def DFS(v):
    # 현재 노드 방문 처리
    visited[v] = 1
    print(v, end=' ')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in range(1, N + 1):
        if visited[i] == 0 and graph[v][i] == 1:
            DFS(i)

# def DFS(x):
#     visited = [0 for _ in range(N + 1)]
#     stack = [x]
#     while stack:
#         cur = stack.pop()
#         if visited[cur] == 1:
#             return
#         else:
#             dfs.append(cur)
#             visited[cur] = 1
#             temp = []
#             for i in range(len(graph[cur])):
#                 if graph[cur][i] == 1 and i not in dfs:
#                     temp.append(i)
#             temp.sort(reverse=True)
#             stack.extend(temp)

def BFS(x):
    visited = [0 for _ in range(N + 1)]
    bfs.append(x)
    stack = [x]
    while stack:
        cur = stack.pop(0)
        if visited[cur] == 1:
            return
        else:
            visited[cur] = 1
            for i in range(len(graph[cur])):
                if graph[cur][i] == 1 and visited[i] == 0 and i not in bfs:
                    stack.append(i)
                    bfs.append(i)
                    

DFS(V)
BFS(V)
for i in range(len(dfs)):
    print(dfs[i], end=' ')
print()
for i in range(len(bfs)):
    print(bfs[i], end=' ')
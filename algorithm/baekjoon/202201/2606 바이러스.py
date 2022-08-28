N = int(input())
K = int(input())

graph = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(K):
    A, B = map(int, input().split())
    graph[A][B] = 1
    graph[B][A] = 1

visited = [0] * (N + 1)
result = 0
def find():
    global result
    q = [1]
    visited[1] = 1
    while q:
        cur = q.pop(0)
        visited[cur] = 1
        for i in range(len(graph[cur])):
            if graph[cur][i] == 1 and visited[i] == 0 and i not in q:
                q.append(i)
                result += 1


find()
print(result)
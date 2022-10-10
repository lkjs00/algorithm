N, K = map(int, input().split())
arr = [0] * 100001
def BFS():
    q = [N]
    while q:
        cur = q.pop(0)
        if cur == K:
            print(arr[K])

        for i in (cur - 1, cur + 1, cur * 2):
            if 0 <= i <= 100000 and not arr[i]:
                arr[i] = arr[cur] + 1
                q.append(i)

BFS()
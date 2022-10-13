N = int(input())
arr = [0] * 1000001
def BFS():
    q = [N]
    while q:
        cur = q.pop(0)
        if cur == 1:
            print(arr[:10])

        if cur % 3 == 0 and cur % 2 == 0:
            for i in (cur // 3, cur // 2, cur - 1):
                if 0 <= i <= 1000000 and not arr[i]:
                    arr[i] = arr[cur] + 1
                    q.append(i)
        elif cur % 3 == 0 and cur % 2 != 0:
            for i in (cur // 3, cur - 1):
                if 0 <= i <= 1000000 and not arr[i]:
                    arr[i] = arr[cur] + 1
                    q.append(i)
        elif cur % 3 != 0 and cur % 2 == 0:
            for i in (cur // 2, cur - 1):
                if 0 <= i <= 1000000 and not arr[i]:
                    arr[i] = arr[cur] + 1
                    q.append(i)
        elif cur % 3 != 0 and cur % 2 != 0:
            if 0 <= cur - 1 <= 1000000 and not arr[cur - 1]:
                arr[i] = arr[cur] + 1
                q.append(i)

BFS()
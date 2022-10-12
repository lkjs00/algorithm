N, M = map(int, input().split())
tree = list(map(int, input().split()))

start = 0
end = max(tree)

while start <= end:
    answer = 0
    mid = (start + end) // 2

    for i in tree:
        if i > mid:
            answer += (i - mid)
        if answer >= M:
            break

    if answer >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)
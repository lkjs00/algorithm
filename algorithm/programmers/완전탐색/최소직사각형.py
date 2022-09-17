def solution(sizes):
    answer = 0
    N = len(sizes)

    def find(tmp_arr, n, max_val):
        if n == N - 1:
            x = []
            y = []
            for i in range(N):
                x.append(tmp_arr[i][0])
                y.append(tmp_arr[i][1])
            if max(x) * max(y) >= max_val:
                max_val = max(x) * max(y)
            return max_val
        tmp_arr.append([sizes[n + 1][0], sizes[n + 1][1]])
        find(tmp_arr, n + 1, max_val)
        tmp_arr.pop()
        tmp_arr.append([sizes[n + 1][1], sizes[n + 1][0]])
        find(tmp_arr, n + 1, max_val)
        tmp_arr.pop()

    answer = find([sizes[0]], 0, 0)
    [sizes[0]].reverse()
    answer = find([sizes[0]], 0, 0)

    return answer

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))

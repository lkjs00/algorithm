N, K = map(int, input().split())
arr = list(map(int, input().split()))

max_val = sum(arr[:K])
start = 0
end = K
tmp_sum = sum(arr[:K])
for _ in range(N - K):
    tmp_sum = tmp_sum - arr[start] + arr[end]
    if tmp_sum > max_val:
        max_val = tmp_sum
    start += 1
    end += 1

print(max_val)
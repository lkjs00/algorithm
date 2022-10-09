X, Y, W, S = map(int, input().split())

if 2 * W > S:
    answer = (min(X, Y) * S) + (abs(X - Y) * W)
else:
    answer = (X + Y) * W
print(answer)
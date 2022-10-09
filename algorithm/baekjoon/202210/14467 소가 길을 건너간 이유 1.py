N = int(input())

answer = 0
road = {}
for _ in range(N):
    cow, location = map(int, input().split())
    if cow not in road:
        road[cow] = location
    else:
        if road[cow] == location:
            continue
        else:
            road[cow] = location
            answer += 1

print(answer)
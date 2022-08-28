def solution(money, costs):
    answer = 0
    value = [[costs[0] * 500, 1], [costs[1] * 100, 5], [costs[2] * 50, 10], [costs[3] * 10, 50], [costs[4] * 5, 100], [costs[5], 500]]
    value.sort(key=lambda x : x[0], reverse=False)

    while True:
        if money == 0: break
        if money // value[0][1] > 0:
            answer += ((money // value[0][1]) * (value[0][0] // (500 // (value[0][1]))))
            money -= (value[0][1] * (money // value[0][1]))
            value.pop(0)
    return answer

print(solution(4578, [1, 4, 99, 35, 50, 1000]))
#print(solution(1999, [2, 11, 20, 100, 200, 600]))
def solution(goods):
    answer = []

    for i in range(len(goods)):
        good = []
        tmp = 0
        while True:
            if len(good) != 0: break
            if tmp == len(goods[i]):
                good.append("None")
                break
            for j in range(len(goods[i]) - tmp):
                srch = goods[i][j:j+tmp+1]
                cnt = 0
                for k in range(len(goods)):
                    if i == k: continue
                    else:
                        if srch in goods[k]:
                            cnt += 1
                if cnt == 0 and srch not in good:
                    good.append(srch)
            tmp += 1
        answer.append(good)

    result = []
    for i in range(len(answer)):
        answer[i].sort()
        tmp = ""
        for j in range(len(answer[i])):
            if j == len(answer[i]) - 1:
                tmp += answer[i][j]
            else:
                tmp += answer[i][j] + " "
        result.append(tmp)
    

        
    return result

solution(["pencil","cilicon","contrabase","picturelist"])
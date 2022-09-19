def solution(new_id):
    answer = ''

    first = ''
    # 1단계
    for idx in range(len(new_id)):
        if 65 <= ord(new_id[idx]) <= 90:
            first += chr(ord(new_id[idx]) + 32)
        else:
            first += new_id[idx]

    second = ''
    # 2단계
    for idx in range(len(first)):
        if 97 <= ord(first[idx]) <= 122:
            second += first[idx]
        elif 48 <= ord(first[idx]) <= 57:
            second += first[idx]
        elif ord(first[idx]) == 45 or ord(first[idx]) == 95 or ord(first[idx]) == 46:
            second += first[idx]

    third = ''
    # 3단계
    flag = True
    for idx in range(len(second)):
        if ord(second[idx]) == 46 and flag == True:
            third += second[idx]
            flag = False
        elif ord(second[idx]) == 46 and flag == False:
            pass
        elif ord(second[idx]) != 46 and flag == False:
            third += second[idx]
            flag = True
        elif ord(second[idx]) != 46 and flag == True:
            third += second[idx]

    fourth = ''
    # 4단계
    if ord(third[0]) == 46:
        third = third[1:]
    if len(third) > 0:
        if ord(third[-1]) == 46:
            third = third[:-1]
    fourth = third

    fifth = ''
    # 5단계
    if len(fourth) == 0:
        fifth = 'a'
    else:
        fifth = fourth
    print(fifth)
    sixth = ''
    # 6단계
    if len(fifth) >= 16:
        sixth = fifth[:15]
    else:
        sixth = fifth
    if ord(sixth[-1]) == 46:
        sixth = sixth[0:-1]
    seventh = ''
    # 7단계
    if len(sixth) == 1:
        seventh = sixth + sixth + sixth
    elif len(sixth) == 2:
        seventh = sixth + sixth[-1]
    else:
        seventh = sixth
    return seventh

print(solution("abcdefghijklmn.p"))
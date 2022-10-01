def solution(registered_list, new_id):
    answer = ''
    if new_id not in registered_list:
        answer = new_id
    else:
        while new_id in registered_list:
            registered_list.remove(new_id)
            tmp_num = 0
            for idx in range(len(new_id)):
                if new_id[idx].isdigit():
                    tmp_num += 1
                    S, N = new_id[:idx], new_id[idx:]
                    break
            if tmp_num == 0:
                S = new_id
                N = ''
            if len(N) == 0:
                N = 0
            else:
                N = int(N)
            N1 = N + 1
            new_id = S + str(N1)
            answer = S + str(N1)
    return answer

print(solution(["card", "ace13", "ace165", "banker", "ace17", "ace14"], "ace165"))
print(solution(["cow", "cow1", "cow2", "cow3", "cow4", "cow5", "cow6", "cow7", "cow8", "cow9"], "cow"))
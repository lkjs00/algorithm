def solution(arr, processes):
    new_processes = []
    for process in processes:
        process = list(map(str, process.split()))
        for i in range(1, len(process)):
            process[i] = int(process[i])
        new_processes.append(process)

    answer = []
    wait = []
    todo = []
    seconds = 1
    todo.append(new_processes.pop(0))
    if todo[0][0] == 'read':
        tmp = ''
        for i in range(todo[0][3], todo[0][4] + 1):
            tmp += arr[i]
        answer.append(tmp)

    cnt = 0
    while todo or wait or new_processes:
        seconds += 1
        # 할 일이 있으면 사용시간 +1
        if todo: cnt += 1
        # 기다렸으니까 대기process 시작시간을 +1
        if len(wait) > 0:
            for i in range(len(wait)):
                wait[i][1] += 1

        for i in range(len(todo) - 1, -1, -1):
            if todo[i][1] + todo[i][2] == seconds:
                if todo[i][0] == 'read':
                    del todo[i]
                elif todo[i][0] == 'write':
                    for j in range(todo[i][3], todo[i][4] + 1):
                        arr[j] = str(todo[i][5])
                    todo.remove(todo[i])


        if len(new_processes) > 0 and new_processes[0][1] == seconds:
            if new_processes[0][0] == 'read':
                if len(wait) > 0:
                    wait.append(new_processes.pop(0))
                else:
                    tmp = ''
                    for i in range(new_processes[0][3], new_processes[0][4] + 1):
                        tmp += arr[i]
                    answer.append(tmp)
                    todo.append(new_processes.pop(0))
            elif new_processes[0][0] == 'write':
                if len(wait) > 0:
                    wait.append(new_processes.pop(0))
                    wait.sort(key=lambda x : x[0], reverse=True)
                else:
                    if len(todo) > 0:
                        wait.append(new_processes.pop(0))
                        wait.sort(key=lambda x : x[0], reverse=True)
                    else:
                        todo.append(new_processes.pop(0))


            # if len(todo) > 0 and todo[0][0] == 'read' and new_processes[0][0] == 'read':
            #     if len(wait) == 0:
            #         tmp = ''
            #         for i in range(new_processes[0][3], new_processes[0][4] + 1):
            #             tmp += arr[i]
            #         answer.append(tmp)
            #         todo.append(new_processes.pop(0))
            #     else:
            #         wait.append(new_processes.pop(0))
            # elif new_processes[0][0] == 'write':
            #     wait.append(new_processes.pop(0))
            #     wait.sort(key=lambda x : x[0], reverse=True)
            # elif len(todo) > 0 and todo[0][0] == 'write' and new_processes[0][0] == 'read':
            #     wait.append(new_processes.pop(0))
            # elif len(todo) == 0 and new_processes[0][0] == 'read':
            #     tmp = ''
            #     for i in range(new_processes[0][3], new_processes[0][4] + 1):
            #         tmp += arr[i]
            #     answer.append(tmp)
            #     todo.append(new_processes.pop(0))


        if len(todo) == 0 and len(wait) > 0:
            while True:
                if wait[0][0] == 'write':
                    todo.append(wait.pop(0))
                    break
                else:
                    tmp = ''
                    for i in range(wait[0][3], wait[0][4] + 1):
                        tmp += arr[i]
                    answer.append(tmp)
                    todo.append(wait.pop(0))
                if len(wait) == 0: break
        
    answer.append(str(cnt))
            
        
    return answer

#solution(["1","2","4","3","3","4","1","5"], ["read 1 3 1 2","read 2 6 4 7","write 4 3 3 5 2","read 5 2 2 5","write 6 1 3 3 9", "read 9 1 0 7"])
solution(["1","1","1","1","1","1","1"], ["write 1 12 1 5 8","read 2 3 0 2","read 5 5 1 2","read 7 5 2 5","write 13 4 0 1 3","write 19 3 3 5 5","read 30 4 0 6","read 32 3 1 5"])
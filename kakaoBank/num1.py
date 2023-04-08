def solution(logs):
    logArray = logs.split('\n')

    answer = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for l in logArray:
        tempStr = l.split(' ')[1].split(':')[0]
        tempStr = int(tempStr)
        tempStr += 9
        if tempStr >= 24:
            tempStr = tempStr % 24

        answer[tempStr] = answer[tempStr] + 1

    return answer
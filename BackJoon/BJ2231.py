N = int(input())
answer = 1
flag = True
while answer <= N:
    tempAnswer = answer
    tempList = str(answer)
    for i in tempList:
        tempAnswer += int(i)
    if tempAnswer == N:
        print(answer)
        flag = False
        break
    answer += 1
if flag:
    print(0)
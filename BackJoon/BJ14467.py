N = int(input())
acrossList = [[],[],[],[],[],[],[],[],[],[]]

for i in range(N):
    num, location = map(int, input().split())
    acrossList[num-1].append(location)

answer = 0

for inputList in acrossList:
    arraySize = len(inputList)
    if arraySize <= 1:
        continue
    else:
        tempAnswer = 0
        for i in range(1, len(inputList)):
            if inputList[i-1] != inputList[i]:
                tempAnswer+=1
        answer += tempAnswer

print(answer)

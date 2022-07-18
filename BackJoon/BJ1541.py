'''
    -를 기준으로 그 사이값들을 각각 다 계산한 후에 맨 앞에수에서 그 후 마이너스 전까지의 그룹을 모두 뺀다.
'''
inputCharList = list(input())

tempNumList = []
minusList = []
tempNum = 0
answer = 0

def makeNum(l=[]):
    num = 0
    for i in range(len(l)):
        l[i] = int(l[i])
        num += l[i] * (10**(len(l)-i-1))
    return num

for c in inputCharList:
    if c == '+':
        tempNum += makeNum(tempNumList)
        tempNumList.clear()
    elif c == '-':
        tempNum += makeNum(tempNumList)
        tempNumList.clear()

        minusList.append(tempNum)
        tempNum = 0
    else:
        tempNumList.append(c)
tempNum += makeNum(tempNumList)
minusList.append(tempNum)

for i in minusList:
    answer -= i

answer += minusList[0]
answer += minusList[0]

print(answer)



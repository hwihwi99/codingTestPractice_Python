from collections import deque
str = input()

str = str.replace(';','')
str = str.replace(',','')
strList = list(str.split())

typeStr = ''
defaultSign = []
for c in strList[0]:
    if c.isalpha():
        typeStr += c
    elif c == ']':
        continue
    else:
        defaultSign.append(c)


defaultSignStr = ''
for i in range(0,len(defaultSign)):
    if defaultSign[i] == '[':
        defaultSignStr += '[]'
    else:
        defaultSignStr += defaultSign[i]



answer = []

for var in range(1,len(strList)):
    variableName = ''
    signList = []

    for c in strList[var]:
        if c.isalpha():
            variableName += c
        elif c == ']':
            continue
        else:
            signList.append(c)

    answer = ''
    answer += typeStr
    answer += defaultSignStr
    # TODO : 값 구하기
    lengthArr = len(signList)
    for i in reversed(range(lengthArr)):
        tempC = signList[i]

        if tempC == '[':
            answer += '[]'
        else:
            answer += tempC

    answer += ' '
    answer += variableName
    answer += ';'
    print(answer)



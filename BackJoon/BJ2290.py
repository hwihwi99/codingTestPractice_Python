s, n = map(str,input().split())
s = int(s)
answerArr = []
for i in range(2*s + 3):
    answerArr.append([])


def drawOne():
    for i in range(2 * s + 3):
        for j in range(s + 2):
            if i == 0 or i == 2 * s + 2 or i == s + 1:
                answerArr[i].append(' ')
            else:
                if j == s + 1:
                    answerArr[i].append('|')
                else:
                    answerArr[i].append(' ')
        answerArr[i].append(' ')


def drawTwo():
    for i in range(2 * s + 3):
        for j in range(s + 2):
            if i == 0 or i == 2 * s + 2 or i == s + 1:
                if j == 0 or j == s+1:
                    answerArr[i].append(' ')
                else:
                    answerArr[i].append('-')
            elif i in range(1,s+1):
                if j == s + 1:
                    answerArr[i].append('|')
                else:
                    answerArr[i].append(' ')
            else:
                if j == 0:
                    answerArr[i].append('|')
                else:
                    answerArr[i].append(' ')
        answerArr[i].append(' ')

def drawThree():
    for i in range(2 * s + 3):
        for j in range(s + 2):
            if i == 0 or i == 2 * s + 2 or i == s + 1:
                if j == 0 or j == s+1:
                    answerArr[i].append(' ')
                else:
                    answerArr[i].append('-')
            else :
                if j == s + 1:
                    answerArr[i].append('|')
                else:
                    answerArr[i].append(' ')
        answerArr[i].append(' ')

def drawFour():
    for i in range(2 * s + 3):
        for j in range(s + 2):
            if i == 0 or i == 2 * s + 2:
                answerArr[i].append(' ')
            elif i == s + 1:
                if j == 0 or j == s+1:
                    answerArr[i].append(' ')
                else:
                    answerArr[i].append('-')
            elif i in range(1,s+1):
                if j == 0 or j == s+1:
                    answerArr[i].append('|')
                else:
                    answerArr[i].append(' ')
            else :
                if j == s + 1:
                    answerArr[i].append('|')
                else:
                    answerArr[i].append(' ')
        answerArr[i].append(' ')

def drawFive():
    for i in range(2 * s + 3):
        for j in range(s + 2):
            if i == 0 or i == 2 * s + 2 or i == s + 1:
                if j == 0 or j == s+1:
                    answerArr[i].append(' ')
                else:
                    answerArr[i].append('-')
            elif i in range(1,s+1):
                if j == 0:
                    answerArr[i].append('|')
                else:
                    answerArr[i].append(' ')
            else:
                if j == s+1:
                    answerArr[i].append('|')
                else:
                    answerArr[i].append(' ')
        answerArr[i].append(' ')

def drawSix():
    for i in range(2 * s + 3):
        for j in range(s + 2):
            if i == 0 or i == 2 * s + 2 or i == s + 1:
                if j == 0 or j == s+1:
                    answerArr[i].append(' ')
                else:
                    answerArr[i].append('-')
            elif i in range(1,s+1):
                if j == 0:
                    answerArr[i].append('|')
                else:
                    answerArr[i].append(' ')
            else:
                if j == s+1 or j == 0:
                    answerArr[i].append('|')
                else:
                    answerArr[i].append(' ')
        answerArr[i].append(' ')

def drawSeven():
    for i in range(2 * s + 3):
        for j in range(s + 2):
            if i == 0:
                if j == 0 or j == s+1:
                    answerArr[i].append(' ')
                else:
                    answerArr[i].append('-')
            elif i == s+1 or i == 2*s+2:
                answerArr[i].append(' ')
            else:
                if j == s+1:
                    answerArr[i].append('|')
                else:
                    answerArr[i].append(' ')
        answerArr[i].append(' ')

def drawEight():
    for i in range(2 * s + 3):
        for j in range(s + 2):
            if i == 0 or i == 2 * s + 2 or i == s + 1:
                if j == 0 or j == s+1:
                    answerArr[i].append(' ')
                else:
                    answerArr[i].append('-')
            else:
                if j == s+1 or j == 0:
                    answerArr[i].append('|')
                else:
                    answerArr[i].append(' ')
        answerArr[i].append(' ')

def drawNine():
    for i in range(2 * s + 3):
        for j in range(s + 2):
            if i == 0 or i == 2 * s + 2 or i == s + 1:
                if j == 0 or j == s+1:
                    answerArr[i].append(' ')
                else:
                    answerArr[i].append('-')
            elif i in range(1,s+1):
                if j == 0 or j == s+1:
                    answerArr[i].append('|')
                else:
                    answerArr[i].append(' ')
            else:
                if j == s+1:
                    answerArr[i].append('|')
                else:
                    answerArr[i].append(' ')
        answerArr[i].append(' ')

def drawZero():
    for i in range(2 * s + 3):
        for j in range(s + 2):
            if i == 0 or i == 2 * s + 2:
                if j == 0 or j == s+1:
                    answerArr[i].append(' ')
                else:
                    answerArr[i].append('-')
            elif i == s+1:
                answerArr[i].append(' ')
            else:
                if j == s+1 or j == 0:
                    answerArr[i].append('|')
                else:
                    answerArr[i].append(' ')
        answerArr[i].append(' ')

def drawNum(n):
    if n == '0':
        drawZero()
    elif n == '1':
        drawOne()
    elif n == '2':
        drawTwo()
    elif n == '3':
        drawThree()
    elif n == '4':
        drawFour()
    elif n == '5':
        drawFive()
    elif n == '6':
        drawSix()
    elif n == '7':
        drawSeven()
    elif n == '8':
        drawEight()
    elif n == '9':
        drawNine()

num=''

for c in n:
    drawNum(c)

for i in range(len(answerArr)):
    for j in range(len(answerArr[0])):
        num += answerArr[i][j]
    num += '\n'
print(num)
strInput = input()
findKeyword = input()

answerStr = ''

for s in strInput:
    if not s.isdigit():
        answerStr += s

if findKeyword in answerStr:
    print(1)
else:
    print(0)
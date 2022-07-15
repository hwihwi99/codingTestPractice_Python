while True:
    inputStr = input()
    if inputStr == ".":
        break
    stack = []
    flag = True
    inputArray = list(inputStr)
    for j in inputArray:
        if j == '(' or j == '[':
            stack.append(j)
        elif j == ')':
            if len(stack) == 0:
                flag = False
                break

            tmp = stack.pop()

            if tmp != '(':
                flag = False
                break

        elif j == ']':
            if len(stack) == 0:
                flag = False
                break

            tmp = stack.pop()
            if tmp != '[':
                flag = False
                break

    if len(stack) != 0:
        flag = False

    if flag:
        print("yes")
    else:
        print("no")
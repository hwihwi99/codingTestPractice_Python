T = int(input())
for i in range(T):
    inputStr = list(input())
    stack = []
    flag = True
    for c in inputStr:
        if c == '(':
            stack.append(c)
        elif c == ')' and len(stack) != 0:
            stack.pop(len(stack)-1)
        elif c == ')' and len(stack) == 0:
            print("NO")
            flag = False
            break

    if flag == True and len(stack) == 0:
        print("YES")
    elif flag == True and len(stack) != 0:
        print("NO")
T = int(input())
for i in range(T):
    inputStr = list(input())
    stack = []
    flag = 1
    for c in inputStr:
        if c == '(':
            stack.append(c)
        elif c == ')' and len(stack) != 0:
            stack.pop(len(stack)-1)
        elif c == ')' and len(stack) == 0:
            print("NO")
            flag = 0
            break

    if flag == 1 and len(stack) == 0:
        print("YES")
    elif flag == 1 and len(stack) != 0:
        print("NO")
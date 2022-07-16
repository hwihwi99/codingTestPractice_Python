N,K = map(int, input().split())
stack = []
for i in range(N):
    stack.append(i+1)
answer = []
while len(stack):
    for j in range(K-1):
        stack.append(stack.pop(0))
    answer.append(stack.pop(0))

print("<", end ='')
for i in range(len(answer) - 1):
    print("%d, "%answer[i], end='')
print(answer[-1], end='')
print(">")
T = int(input())

fibonacciList = []
fibonacciList.append([1,0])
fibonacciList.append([0,1])

for i in range(2,41):
    zero = fibonacciList[i-1][0] + fibonacciList[i-2][0]
    one = fibonacciList[i-1][1] + fibonacciList[i-2][1]
    newList = [zero, one]
    fibonacciList.append(newList)

for i in range(T):
    N = int(input())
    answerList = fibonacciList[N]
    print(answerList[0], end=' ')
    print(answerList[1])
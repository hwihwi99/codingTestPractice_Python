dic = {'ADD':['0000','0'],'ADDC':['0000','1'],'SUB':['0001','0'],'SUBC':['0001','1'],'MOV':['0010','0'],
       'MOVC':['0010','1'],'AND':['0011','0'],'ANDC':['0011','1'],'OR':['0100','0'],'ORC':['0100','1'],
       'NOT':['0101','0'],'MULT':['0110','0'],'MULTC':['0110','1'],'LSFTL':['0111','0'],'LSFTLC':['0111','1'],
       'LSFTR':['1000','0'],'LSFTRC':['1000','1'],'ASFTR':['1001','0'],'ASFTRC':['1001','1'],'RL':['1010','0'],
       'RLC':['1010','1'],'RR':['1011','0'],'RRC':['1011','1']}

def binaryNum(n):
    bitArr = []
    while n>0:
        bitArr.append(n%2)
        n = n //2

    bitArr.reverse()
    answer = ''
    for i in range(len(bitArr)):
        answer += str(bitArr[i])

    return answer

T = int(input())
for i in range(T):
    inputArr = input().split()
    fourBit = dic[inputArr[0]][1]
    answer = ''
    answer += dic[inputArr[0]][0] # 0 ~ 3
    answer += dic[inputArr[0]][1] # 4
    answer += '0' # 5

    for i in range(1, len(inputArr)):
        num = int(inputArr[i])
        tempAns = binaryNum(num)
        if i == 3 and fourBit == '1':
            diff = 4 - len(tempAns)
            tempStr = ''
            for j in range(diff):
                tempStr += '0'
            tempStr += tempAns
            answer += tempStr
        elif i == 3 and fourBit == '0':
            diff = 3 - len(tempAns)
            tempStr = ''
            for j in range(diff):
                tempStr += '0'
            tempStr += tempAns
            tempStr += '0'
            answer += tempStr
        elif i == 1 or i == 2:
            diff = 3 - len(tempAns)
            tempStr = ''
            for j in range(diff):
                tempStr += '0'
            tempStr += tempAns
            answer += tempStr
    print(answer)




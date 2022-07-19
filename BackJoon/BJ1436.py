'''
나는 아무래도 브루트포스만 보면 겁을 먹는 것 같다.
그냥 쭉 노가다를 하면 되는 어쩌면 더 단순한 문제인데..
'''
answer = 666
N = int(input())

while N != 0:
    tempStr = str(answer)
    if '666' in tempStr:
        N = N - 1
    answer= answer + 1

print(answer-1)

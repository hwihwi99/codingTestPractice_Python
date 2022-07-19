N = int(input())
time = list(map(int, input().split()))
time = sorted(time)
answer = 0
tempWaitTime = 0
for i in time:
    answer += (tempWaitTime+i)
    tempWaitTime += i
print(answer)
N, M = map(int, input().split())
cardList = list(map(int, input().split()))

answer = 0
tmp = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1, N):
            tmp = cardList[i]+cardList[j]+cardList[k]
            if tmp<=M and abs(tmp-M) < abs(answer-M):
                answer = tmp
print(answer)





N,K=map(int, input().split())
tmp = N
answer = 1
for i in range(K):
    answer *= tmp
    answer = answer // (i+1)
    tmp -= 1
print(answer)
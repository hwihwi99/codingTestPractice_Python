N,K = map(int, input().split())

coinList = []
for i in range(N):
    coinList.append(int(input()))

coinList = sorted(coinList, reverse=True)

answer = 0

for coin in coinList:
    if K // coin != 0:
        answer += (K//coin)
        K %= coin

    if K == 0:
        break

print(answer)
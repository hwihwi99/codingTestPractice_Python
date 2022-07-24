N,K = map(int,input().split())

dy = []
for i in range(K+1):
    dy.append(0)

for i in range(N):
    W, V = map(int, input().split())
    for j in range(K,W-1,-1):
        dy[j] = max(dy[j], dy[j-W] + V)
print(dy[K])

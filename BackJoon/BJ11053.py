N = int(input())
A = list(map(int, input().split()))

dy = []
for i in range(N):
    dy.append(1)

for j in range(N):
    for k in range(j):
        if A[k] < A[j]:
            dy[j] = max(dy[k] + 1, dy[j])

print(max(dy))
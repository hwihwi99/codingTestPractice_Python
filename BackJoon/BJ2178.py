from collections import deque
N,M = map(int, input().split())
arr = [] # y,x

for i in range(N):
    arr.append(list(map(int, list(input()))))

dx = [-1,1,0,0]
dy = [0,0,1,-1]

queue = deque()
queue.append([0,0])
while queue:
    temp = queue.popleft()
    x = temp[0]
    y = temp[1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<M and 0<=ny<N and arr[ny][nx] == 1:
            queue.append([nx,ny])
            arr[ny][nx] = arr[y][x] + 1

print(arr[N-1][M-1])


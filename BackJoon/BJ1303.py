import sys
from collections import deque
N,M = map(int, input().split()) # N : 가로, M : 세로 5,6
arr = []
visited = []

for i in range(M):
    arr.append([])
    visited.append([])

for i in range(M):
    visited[i] = [False] * N
    tempStr = sys.stdin.readline()
    for c in tempStr:
        arr[i].append(c)

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(x,y,team):
    queue = deque()
    queue.append([x,y])
    visited[y][x] = True
    count = 0
    while queue:
        tempList = queue.popleft()
        for i in range(4):
            tx = tempList[0] + dx[i]
            ty = tempList[1] + dy[i]
            if 0<=tx<N and 0<=ty<M and arr[ty][tx] == team and (not visited[ty][tx]):
                queue.append([tx,ty])
                visited[ty][tx] = True
                count += 1
    if count == 0:
        return 1
    return count + 1


white = 0
black = 0
for i in range(M): # y
    for j in range(N): # x
        if not visited[i][j]:
            if arr[i][j] == 'W':
                white += (bfs(j,i,arr[i][j]) ** 2)
            else:
                black += (bfs(j,i,arr[i][j]) ** 2)

print(white, black)


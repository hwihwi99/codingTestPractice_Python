'''
방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고
라는 문구를 못봐서 많은 시간을 썼다... 문제를 잘 읽자...제발..
'''
from collections import deque

N, M, V = map(int, input().split())
graphList = []
visited = [False] * (N + 1)
for i in range(N + 1):
    graphList.insert(i, [])

for i in range(M):
    E1, E2 = map(int, input().split())
    graphList[E1].append(E2)
    graphList[E2].append(E1)

for i in range(N + 1):
    graphList[i] = sorted(graphList[i])

def dfs(start):
    print(start,end=' ')
    visited[start] = True
    for i in graphList[start]:
        if not visited[i]: #i를 방문하지 않았다면
            dfs(i)

def bfs(start):
    queue = deque()
    queue.append(start)
    print(start, end=' ')
    visited[start] = True
    while queue:
        tempNum = queue.popleft();
        for i in graphList[tempNum]:
            if not visited[i]:
                queue.append(i)
                print(i,end = ' ')
                visited[i] = True

dfs(V)
visited = [False] * (N + 1)
print()
bfs(V)

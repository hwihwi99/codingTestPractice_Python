visited = []
sum = 0
def dfs(graph, start):
    global sum
    global visited
    sum += 1
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i)

def solution(n, wires):
    answer = n
    graph = []

    for i in range(n+1):
        graph.append([])

    for i in range(len(wires)):
        first = wires[i][0]
        second = wires[i][1]
        graph[first].append(second)
        graph[second].append(first)

    global sum
    global visited
    for start, end in wires:
        visited = [False] * (n+1)
        visited[end] = True
        sum = 0
        dfs(graph, start)
        # sum에 한쪽의 전력망이 생긴다.

        if abs(sum - (n-sum)) < answer:
            answer = abs(sum - (n-sum))


    return answer

print(solution(9,	[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
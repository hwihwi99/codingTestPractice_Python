from collections import deque
nums = list(map(int, input().split()))
N = nums[0]
M = nums[1]
l = []
for i in range(1,N+1):
    l.append(i)
answer = 0
findNums = list(map(int, input().split()))
deq = deque(l)

for i in findNums:
    index = deq.index(i) # 이렇게만 해도 된다.
    if index <= len(deq)/2:
        answer += (index)
        for j in range(index):
            tmp = deq.popleft()
            deq.append(tmp) # 맨 뒤 추가
        deq.popleft()
    else:
        tmpLen = len(deq)
        move = tmpLen - index;
        answer += (move)
        for j in range(move):
            tmp = deq.pop()
            deq.appendleft(tmp)
        deq.popleft()
print(answer)

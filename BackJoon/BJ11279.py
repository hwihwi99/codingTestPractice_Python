import heapq
import sys

N = int(input())
heap = []
for i in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -num)
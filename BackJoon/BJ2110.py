N,C = map(int, input().split())
arr = [int(input()) for i in range(N)]
arr.sort()
start, end = 1, arr[-1] - arr[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    count = 1
    currentLocate = arr[0]

    for i in range(1, N):
        if arr[i] - currentLocate >= mid:
            count = count + 1
            currentLocate = arr[i]
    if count >= C:  # 찾은 공유기 갯수가 기존 주어진 것 보다 많다면 => 거리를 줄여서 다시 실행
        result = mid
        start = mid + 1
    else:  # 찾은 공유기 갯수가 기존 주어진 것 보다 적다면 => 거리를 늘려서 다시 실행
        end = mid - 1
print(result)
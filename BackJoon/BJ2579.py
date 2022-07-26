N = int(input())
arr = []
arr.insert(0,0)
for i in range(1,N+1):
    arr.insert(i,int(input()))
dp = []
dp.insert(0, 0)
dp.insert(1, arr[1])
if N >= 2:
    dp.insert(2, arr[1] + arr[2])
elif N >= 3:
    for i in range(3,N+1):
        maxNum = max(dp[i-2]+arr[i], dp[i-3]+arr[i-1]+arr[i])
        dp.insert(i,maxNum)

print(dp[N])
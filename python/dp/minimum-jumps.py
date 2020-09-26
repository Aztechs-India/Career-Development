def min_jumps(arr):
    n = len(arr)
    dp = [float("inf") for i in range(n)]
    dp[0]=0
    for i in range(1, n):
        for j in range(0, i):
            max_jumps = arr[j]+j
            if(i<=max_jumps):
                dp[i] = min(dp[i], dp[j]+1)
    print(dp)
    return dp[-1]

arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
arr = [2,3,1,1,4]
arr = [3,2,1,0,4]
print(min_jumps(arr))
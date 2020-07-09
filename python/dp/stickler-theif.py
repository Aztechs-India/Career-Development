#https://practice.geeksforgeeks.org/problems/stickler-theif/0

def max_sum_with_no_consecutive(arr):
    dp = [0 for _ in arr]
    dp[0] = arr[0]
    dp[1] = max(dp[0], arr[1])
    for i in range(2, len(arr)):
        dp[i] = max(dp[i-2]+arr[i], dp[i-1])
    return dp[-1]

print(max_sum_with_no_consecutive([5, 5, 10, 100, 10, 7]))
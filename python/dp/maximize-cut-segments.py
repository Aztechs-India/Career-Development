def is_already_cut(dp, ind):
    if(ind == 0):
        return True
    if(dp[ind] > 0):
        return True
    return False

def maximize_cut_segments(n, x, y, z):
    dp = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        if((i-x) >=0 and is_already_cut(dp, i-x)):
            dp[i] = max(dp[i], 1 + dp[i-x])
        if((i-y) >=0 and is_already_cut(dp, i-y)):
            dp[i] = max(dp[i], 1 + dp[i-y])
        if((i-z) >=0 and is_already_cut(dp, i-z)):
            dp[i] = max(dp[i], 1 + dp[i-z])
    return dp[-1]

print(maximize_cut_segments(5, 5, 3, 2))
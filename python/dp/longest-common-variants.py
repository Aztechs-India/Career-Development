def longest_common_subsequence(string1, string2):
    n, m = len(string1), len(string2)
    dp = [[0 for i in range(n+1)] for i in range(m+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if(string1[i-1] == string2[j-1]):
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print("Dp Array", dp)
    return dp[-1][-1]

def longest_common_substring(string1, string2):
    n, m = len(string1), len(string2)
    print(n, m)
    dp = [[0 for i in range(m+1)] for i in range(n+1)]
    length = float("-inf")
    for i in range(1, n+1):
        for j in range(1, m+1):
            if(string1[i-1] == string2[j-1]):
                dp[i][j] = dp[i-1][j-1]+1
                length = max(length, dp[i][j])
            else:
                dp[i][j] = 0
    print("Dp Array", dp)
    return length

print(longest_common_substring("ABCDGH", "ABCXYZCDGH"))


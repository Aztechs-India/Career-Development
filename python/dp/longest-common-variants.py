def longest_common_subsequence(string1, string2):
    n, m = len(string1), len(string2)
    dp = [[0 for i in range(n+1)] for i in range(m+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if(string1[i-1] == string2[j-1]):
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]

def longest_common_substring(string1, string2):
    n, m = len(string1), len(string2)
    dp = [[0 for i in range(m+1)] for i in range(n+1)]
    length = float("-inf")
    for i in range(1, n+1):
        for j in range(1, m+1):
            if(string1[i-1] == string2[j-1]):
                dp[i][j] = dp[i-1][j-1]+1
                length = max(length, dp[i][j])
            else:
                dp[i][j] = 0
    return length

def longest_palindromic_subsequence(string):
    n = len(string)
    dp = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for i in range(1, n):
        row = 0
        for j in range(0, n):
            end = j + i
            if(end >= n):
                break
            if(string[j] == string[end]):
                dp[row][end] = dp[row+1][end-1]+2
            else:
                dp[row][end] = max(dp[row-1][end], dp[row][end-1])
            row+=1
    return dp[0][-1]

def longest_palindromic_substring(string):
    n = len(string)
    dp = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        dp[i][i] = 1
    maximum = float("-inf")
    for i in range(1, n):
        row = 0
        for j in range(0, n):
            end = j + i
            if(end >= n):
                break
            if(string[j] == string[end] and dp[row+1][end-1] == (end-row-1)):
                dp[row][end] = dp[row+1][end-1]+2
                maximum = max(maximum, dp[row][end])
            else:
                dp[row][end] = 0
            row+=1
    return maximum
#print(longest_common_substring("ABCDGH", "ABCXYZCDGH"))
#print(longest_palindromic_subsequence("NACAMACAN"))
print(longest_palindromic_substring("forgeeksskeegfor"))



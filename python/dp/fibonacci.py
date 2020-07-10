def fibo(n):
    if(n<=1):
        return n
    return fibo(n-1)+fibo(n-2)

def fib_td(n, dp):
    if(n<=1):
        return n
    if(dp[n] == -1):
        dp[n] = fib_td(n-1, dp)+fib_td(n-2, dp)
    return dp[n]

def fib_bu(n):
    dp = [0 for i in range(n)]
    dp[0]=1
    dp[1]=1

    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[-1]

n=7
print(fibo(n))
dp=[-1 for i in range(n+1)]
print(fib_td(n, dp))
print(fib_bu(n))
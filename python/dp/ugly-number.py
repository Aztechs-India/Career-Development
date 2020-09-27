def max_divide(num1, num2):
    while (num1%num2 == 0):
        num1 = num1/num2
    return num1

def is_ugly(num):
    num = max_divide(num, 2)
    num = max_divide(num, 3)
    num = max_divide(num, 5)
    return True if num == 1 else False

def nth_ugly_number(n):
    dp = [0 for i in range(n)]
    dp[0]=1
    
    i=0
    j=0
    k=0
    
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5

    for l in range(1, n):
        print("Loop Start:")
        dp[l] = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
        print(dp[l],next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)

        if(dp[l] == next_multiple_of_2):
            i+=1
            next_multiple_of_2 = dp[i]*2
        
        if(dp[l] == next_multiple_of_3):
            j+=1
            next_multiple_of_3 = dp[j]*3

        if(dp[l] == next_multiple_of_5):
            k+=1
            next_multiple_of_5 = dp[k]*5

        print("End of loop")
        print(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
    
    print(dp)

nth_ugly_number(150)
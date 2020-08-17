def counting_sort(arr):
    maximum = max(arr)
    count = [0 for i in range(maximum+1)]

    for i in arr:
        count[i]+=1

    n = len(count)

    for i in range(1, n):
        count[i] += count[i-1]

    result = [0 for i in arr]

    for i in arr:
        ind = count[i]-1
        result[ind] = i
        count[i]-=1

    print(result)

counting_sort([1, 4, 1, 2, 7, 5, 2])
def common(arr1, arr2, arr3):
    i=0
    j=0
    k=0
    n = len(arr1)
    m = len(arr2)
    o = len(arr3)

    min_index = 0
    result =[]
    while(i<n and j<m and k<o):
        if(arr1[i] == arr2[j] and arr2[j] == arr3[k]):
            result.append(arr1[i])
            
        if(arr1[i] <= arr2[j] and arr1[i] <= arr3[k]):
            i+=1
        elif(arr2[j] <= arr1[i] and arr2[j] <= arr3[k]):
            j+=1
        elif(arr3[k] <= arr1[i] and arr3[k] <= arr2[j]):
            k+=1
    return result

ar1 = [1, 5, 10, 20, 40, 80] 
ar2 = [6, 7, 20, 80, 100] 
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

print(common(ar1, ar2, ar3))
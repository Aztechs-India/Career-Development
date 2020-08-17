from math import ceil

def get_gap(n):
    if(n == 1):
        return 0
    return ceil(n/2.0)

def shell_sort(arr):
    n = len(arr)
    gap = get_gap(n)
    while(gap > 0):
        process_array(arr, gap, n)
        print("SL", arr)
        gap = get_gap(gap)

def process_array(arr, gap, n):
    ind = 0
    while(ind+gap < n):
        if(arr[ind] > arr[ind+gap]):
            arr[ind], arr[ind+gap] = arr[ind+gap], arr[ind]
        ind += 1

arr = [3, 27, 38, 43, 9, 10, 82]
shell_sort(arr)
print("Final Array", arr)
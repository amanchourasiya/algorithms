def search_pivot_point(arr):
    l = 0
    r = len(arr) -1
    
    
    while l <= r:
        m = l + (r - l)//2
        if arr[m-1] < arr[m] > arr[m+1]:
            return m
        if arr[m-1] < arr[m] < arr[m+1]:   # pivot lies in right since elements are in increasing order
            l = m + 1
        elif arr[m-1] > arr[m] > arr[m+1]: # pivot lies in left since elements are in decreasing order
            r = m -1
     

    return -1

def search_element(arr,element):
    pivot_point = search_pivot_point(arr)
    print('pivot',pivot_point)
    l = 0
    r = pivot_point -1 

    if arr[pivot_point] == element:
        return pivot_point

    #searching in first part where values are in increasing order
    while l <= r:
        m = (l + (r-l)//2)
        if arr[m] == element:
            return m
        if element < arr[m]:
            r = m - 1
        else:
            l = m + 1
        
    # Searching in second part where values are in decreasing order
    l = pivot_point + 1
    r = len(arr) -1
    while l <=r:
        m = (l + (r -l)//2)
        if element == arr[m]:
            return m
        if element < arr[m]:
            l = m + 1
        else:
            r = m - 1

    return -1

def test_bitonic():
    a = [1,2,3,4,5,6,4,3,2,1]
    print(search_element(a,52))

test_bitonic()     

        

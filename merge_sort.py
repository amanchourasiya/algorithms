def merge(l_array,r_array):
    i=0
    j=0
    p = len(l_array)
    q = len(r_array)
    res = []

    while (i + j) < (p + q):
        if i >= p:
            res.append(r_array[j])
            j+=1
        elif j >= q:
            res.append(l_array[i])
            i+=1
        elif l_array[i] < r_array[j]:
            res.append(l_array[i])
            i+=1
        else:
            res.append(r_array[j])
            j+=1
    return res

def merge_sort(arr, left, right):
    if right- left <= 1:
        return arr[left:right]
    if right - left > 1:
        mid = (left + right)//2
        L = merge_sort(arr,left,mid)
        R = merge_sort(arr,mid,right)
        return merge(L,R)


def main():
    a = [10,3,6,71,8,21,9,9]
    print(merge_sort(a,0,len(a)))

main()
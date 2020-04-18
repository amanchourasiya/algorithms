def selection_sort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                arr[i] ,arr[j] = arr[j],arr[i]

def test_sort():
    a = [2,4,55,23,56,3,23,4]
    selection_sort(a)
    print(a)

test_sort()
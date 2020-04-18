def insertion_sort(arr):
    for i in range(1,len(arr)):
    
        for j in range(i,0,-1):
            if arr[j-1] > arr[j]:
                arr[j-1] ,arr[j] = arr[j],arr[j-1]
            else:
                break

def test_insertion():
    a = [31,2]
    insertion_sort(a)
    print(a)

test_insertion()
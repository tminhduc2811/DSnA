"""
! Merge sort has time complexity: Θ(nlg(n))
"""
def merge(arr, start, middle, end):
    left_size = middle - start + 1
    right_size = end - middle
    # left_array = [0]*left_size
    # right_size = [0]*right_size
    left_array = arr[start:middle + 1]
    right_array = arr[middle + 1:end + 1]

    # Inititialize variables
    i = 0
    j = 0
    k = start

    while (i < left_size) and (j < right_size):
        if (left_array[i] < right_array[j]):
            arr[k] = left_array[i]
            i += 1
        else:
            arr[k] = right_array[j]
            j += 1
        k += 1
    # Filling the array with leftovers
    while i < left_size:
        arr[k] = left_array[i]
        k += 1
        i += 1
    
    while j < right_size:
        arr[k] = right_array[j]
        k += 1
        j += 1

def merge_sort(array, start, end):
    if (start < end):
        middle = (start + end)//2
        merge_sort(array, start, middle)
        merge_sort(array, middle + 1, end)
        merge(array, start, middle, end)


if __name__=='__main__':
    a = [2, 5, 1, 6, 7, 0, 33, 100, 12, 4, 22, 28, 27, 27]
    print('Array before being sorted: ', a)
    merge_sort(a, 0, len(a) - 1)
    print('Array after being sorted: ', a)

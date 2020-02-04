import merge_sort

def binary_search(arr, start, end, x): # T(n/2) => O(lg(n))
    if start <= end:
        middle = (start + end)//2
        if arr[middle] == x:
            return middle
        if arr[middle] > x:
            return binary_search(arr, start, middle - 1, x)
        if arr[middle] < x:
            return binary_search(arr, middle + 1, end, x)
    return None


if __name__=='__main__':
    a = [2, 5, 1, 6, 7, 0, 33, 100, 12, 4, 22, 28, 27, 27]
    print('Array before being sorted: ', a)
    merge_sort.merge_sort(a, 0, len(a) - 1)
    print('Array after being sorted: ', a)

    # Now let's find the index of 100
    print('Index of 100 is: ', binary_search(a, 0, len(a) - 1, 100))
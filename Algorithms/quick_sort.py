"""
! Quick sort has time complexity: Θ(nlg(n)) in average cases, and O(n^2) in worst case
* Unlike Merge Sort, Quick Sort doesn't use any extra array, the hidden factors of O(nlg(n)) are generally smaller
"""

# Partition
def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1 # pointer to the last element of the left side of the array
    for j in range(start, end):
        if(arr[j] <= pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1

def quick_sort(arr, start, end):
    if start < end:
        q = partition(arr, start, end)
        quick_sort(arr, start, q - 1)
        quick_sort(arr, q + 1, end)


if __name__=='__main__':
    a = [2, 5, 1, 6, 7, 0, 33, 100, 12, 4, 22, 28, 27, 27]
    print('Array before being sorted: ', a)
    quick_sort(a, 0, len(a) - 1)
    print('Array after being sorted: ', a)

def swap(arr, i1, i2):
    temp = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = temp

# INSERTION SORT
def insertion_sort(arr):
    """
    * Ω(n) in best case
    * O(n^2) in worst case
    ! The insertion sort has a linear best case running time i.e., and this is going to occur when the array is already sorted.
    ! The insertion sort has a quadratic worst-case running time i.e., when the array is sorted in the reverse order.
    """
    for i in range(1, len(arr)):
        j = i
        while (j > 1) & (arr[j-1] > arr[j]):
            swap(arr, j - 1, j)
            j = j - 1
    return arr

# BUBBLE SORT
"""
* Ω(n) in best case
* O(n^2) in worst case
"""
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)
    return arr

def optimized_bubble_sort(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)
        if not swapped: # It means that the array is all sorted
            break
    return arr

# COUNTING SORT
"""
* O(n) complexity
! Restriction: Should only contain INTERGER from 0 to K
"""
def counting_sort(arr):
    k = max(arr)
    size = len(arr)
    temp_arr = [0]*(k+1) # Because this array ranging from 0 to k, so there are k+1 elements
    output_arr = [0]*size
    # Step 1, count the number of times an element is appearing in the array
    for i in range(size):
        temp_arr[arr[i]] += 1

    # Step 2, modify the temporary array by adding k-1 element with k element. 
    # For instance, the value of the modified temp_arr at index = 2 is G, then G is the number smaller or equal 2
    for i in range(1, k + 1):
        temp_arr[i] = temp_arr[i] + temp_arr[i - 1]
        
    # Finnaly, we create the output
    for i in range(size - 1, -1, -1):
        output_arr[temp_arr[arr[i]] - 1] = arr[i]
        temp_arr[arr[i]] -= 1
    return output_arr

def main():
    a = [1, 9, 4, 5, 2, 3, 1, 12]
    print('Array before being sorted', a)

    # sortedArray = insertion_sort(a)
    # sortedArray = bubble_sort(a)
    sortedArray = counting_sort(a)
    print('Array after being sorted', sortedArray)

if __name__ == '__main__':
    main()
    

    



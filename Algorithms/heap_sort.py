"""
! Heap sort takes O(n) for building a heap, and O(nlg(n)) for sorting
"""

heap_size = 10
def get_right_child_index(A, index):
    index += 1
    if (((2*index + 1) <= len(A)) and (index >=0)):
        return 2*index
    return -1

def get_left_child_index(A, index):
    index += 1
    if (((2*index) <= len(A)) and (index >= 0)):
        return 2*index - 1
    return -1

def get_parent_index(A, index):
    if ((index > 1) and (index < len(A))):
        return index//2 # Floor
    return - 1

def max_heapify(A, index):
    left_child_index = get_left_child_index(A, index)
    right_child_index = get_right_child_index(A, index)

    # Find largest among these 3 indexes
    largest = index

    if ((left_child_index > 0) and (left_child_index < heap_size) and (A[left_child_index] > A[largest])):
        largest = left_child_index
    if ((right_child_index > 0) and (right_child_index < heap_size) and (A[right_child_index] > A[largest])):
        largest = right_child_index
    
    # If the node is not the largest, it is not a heap
    if largest != index:
        A[index], A[largest] = A[largest], A[index]
        max_heapify(A, largest)

def min_heapify(A, index):
    left_child_index = get_left_child_index(A, index)
    right_child_index = get_right_child_index(A, index)

    # Find minimum among these 3 indexes
    minimum = index
    
    if ((left_child_index > 0) and (left_child_index < heap_size) and (A[left_child_index] < A[minimum])):
        minimum = left_child_index
    if ((right_child_index > 0) and (right_child_index < heap_size) and (A[right_child_index] < A[minimum])):
        minimum = right_child_index
    
    if minimum != index:
        A[index], A[minimum] = A[minimum], A[index]
        min_heapify(A, minimum)

def build_max_heap(A):
    for i in range(heap_size//2, -1, -1):
        max_heapify(A, i)

def build_min_heap(A):
    for i in range(heap_size//2, -1, -1):
        min_heapify(A, i)

def max_heap_sort(A): #O(nlg(n))
    global heap_size
    while(heap_size > 0): # O(n)
        A[0], A[heap_size - 1] = A[heap_size - 1], A[0]
        heap_size -= 1
        max_heapify(A, 0) # O(logn)

def min_heap_sort(A):
    global heap_size
    while(heap_size > 0):
        A[0], A[heap_size - 1] = A[heap_size - 1], A[0]
        heap_size -= 1
        min_heapify(A, 0)

if __name__=='__main__':
    # Index
    A = [15, 20, 7, 9, 5, 8, 6, 10, 2, 1]
    build_max_heap(A)
    max_heap_sort(A)
    print('Ascending: ', A)

    heap_size = 10
    build_min_heap(A)
    min_heap_sort(A)
    print('Descending: ', A)
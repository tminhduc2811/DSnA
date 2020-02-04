"""
Input Array A[n]
Update(A, l, r, x), l is the starting index, and r is the ending index
If we use 2 loops, the function will have O(nxm) which is very slow for large number of queries and size of the array
So we use Difference Array to update queries
"""

def init_array_D(A):
    n = len(A)
    D = [0]*(n + 1)
    D[0], D[n] = A[0], 0

    for i in range(1, n):
        D[i] = A[i] - A[i - 1]
    
    return D

def update_D(D, left, right, x):
    D[left] += x
    D[right + 1] -= x


def update(A, D):
    A[0] = D[0]
    for i in range(1, len(A)):
        A[i] = A[i - 1] + D[i]

if __name__=='__main__':
    A = [ 10, 5, 20, 40 ]
    D = init_array_D(A)
    update_D(D, 0, 1, 10)
    update(A, D)
    print(A)
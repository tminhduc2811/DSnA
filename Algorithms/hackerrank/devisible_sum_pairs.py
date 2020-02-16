"""
    Given an array A = [1, 2, 3, 4, 5, 6] and k = 5. Find and print the number of pairs which have total is devisible by k
    eg. [1,4], [2,3], [4,6]
    ! Solution:
    eg. k = 3
    Find all the numbers that belong to 3 groups
    1. mod 3 == 0
    2. mod 3 == 1
    3. mod 3 == 2

    * Group 1 will have n! pairs (n! = n(n-1)/2)
    * Group 2 will match with group 3 to satisfy the requirement, there will be n*m pairs, 
    * with n, m are len(group2) and len(group3), respectively
"""

def solution(arr, k):
    temp = [0]*k
    for i in arr:
        temp[i % k] += 1
    # Count the numbers of pair
    count = 0
    for i in range(int(k/2) + 1):
        if i == 0:
            count += int(temp[0]*(temp[0] - 1)/2)
        elif float(i) == (k/2):
            count += int(temp[int(k/2)]*(temp[int(k/2)] - 1)/2)
        else:
            count += int(temp[i]*temp[k-i])
    print(count)

if __name__=='__main__':
    arr = [1, 3, 2, 6, 1, 2]
    solution(arr, 3)
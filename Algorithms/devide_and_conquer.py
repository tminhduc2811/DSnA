def increase_arr(A, start, end):
    if start < end:
        middle = (start + end)//2
        increase_arr(A, start, middle)
        increase_arr(A, middle + 1, end)
    else:
        A[start] += 1

if __name__=='__main__':

    A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    increase_arr(A, 0, len(A) - 1)
    print(A)
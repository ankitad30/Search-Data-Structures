# BINARY SEARCH ITERATIVE

def BS(A,x):
    start =0
    end = len(A) -1

    while (start<= end):
        mid = (start+end)//2
        if (A[mid] ==x):
            return mid
        elif (x < A[mid]):
            end = mid -1
        else:
            start = mid+1
    return -1 # Element not found

A1 =[0, 1, 2, 8, 13, 17, 19, 32, 42]
print(BS(A1, 13))

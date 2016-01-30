#Binary Search Recursive

def binarySearch(alist, item):
        if len(alist) == 0:
            print("Element not in list")
        else:
            midpoint = len(alist)//2
            if alist[midpoint]==item:
              return midpoint
            else:
                if item<alist[midpoint]:
                    return binarySearch(alist[:midpoint],item)
                else:
                    return binarySearch(alist[midpoint+1:],item)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 32))

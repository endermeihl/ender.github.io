def binarySearch(target,sotedlist):
    left = 0
    right = len(sotedlist)-1
    while left <= right:
        mid = (left+right)//2
        if target == sotedlist[mid]:
            return mid
        elif target < sotedlist[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1
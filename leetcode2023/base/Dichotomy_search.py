def dichotomy_search(arr,search_element)->int:
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == search_element:
            return mid
        elif arr[mid] < search_element:
            low = mid + 1
        else:
            high = mid - 1
    return -1
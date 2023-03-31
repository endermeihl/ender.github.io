def merge_sorted_arrays(arr1,arr2):
    i = 0
    j = 0
    result = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    if i < len(arr1):
        result.extend(arr1[i:])
    if j < len(arr2):
        result.extend(arr2[j:])
    return result

arr1 = [1, 3, 5, 7, 9]
arr2 = [2, 4, 6, 8, 10]
result = merge_sorted_arrays(arr1, arr2)
print(result)

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

def findMedianSortedArrays(nums1, nums2) -> float:
    # merge two sorted arrays
    i = 0
    j = 0
    result = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            result.append(nums1[i])
            i += 1
        else:
            result.append(nums2[j])
            j += 1
    if i < len(nums1):
        result.extend(nums1[i:])
    if j < len(nums2):
        result.extend(nums2[j:])
    # print(result)
    # find the median
    if len(result) % 2 == 0:
        return (result[len(result) // 2] + result[len(result) // 2 - 1]) / 2
    else:
        return result[len(result) // 2]


arr1 = [1,2,3]
arr2 = [3]
result = findMedianSortedArrays(arr1, arr2)
print(result)

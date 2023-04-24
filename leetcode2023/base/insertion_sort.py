def insertionSort(lyst):
    i = 1
    while i<len(lyst):
        temp = lyst[i]
        j = i-1
        while j>=0:
            if temp <lyst[j]:
                lyst[j+1] = lyst[j]
                j -= 1
            else:
                break
        lyst[j+1] = temp
        i += 1
        
lyst = [10, 9, 8, 7, 6, 5, 1, 3, 2, 4]  # create a 10 length array with unsorted values
insertionSort(lyst)  # sort the array using the insertionSort function
print(lyst)  # print the sorted array

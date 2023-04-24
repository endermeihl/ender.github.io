def bubbleSort(lyst):
    n = len(lyst)
    for i in range(n-1):
        for j in range(n-1-i):
            if lyst[j]>lyst[j+1]:
                lyst[j],lyst[j+1] = lyst[j+1],lyst[j]


lyst = [1,2,3,4,5,6,7,8,9,10]
bubbleSort(lyst)
print(lyst)
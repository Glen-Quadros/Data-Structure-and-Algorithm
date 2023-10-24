def insertionSort(customList):
    for i in range(1, len(customList)):
        j = i
        while customList[j-1] > customList[j] and j > 0:
            customList[j-1], customList[j] = customList[j], customList[j-1]
            j -= 1
    print(customList)

customList = [9, 7, 5, 3, 1]   
insertionSort(customList)
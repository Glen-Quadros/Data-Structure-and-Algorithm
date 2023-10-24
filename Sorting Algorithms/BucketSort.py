import math

def insertionSort(customList):
    for i in range(1, len(customList)):
        j = i
        while j > 0 and customList[j-1] > customList[j]:
            customList[j-1], customList[j] = customList[j], customList[j-1]
            j -= 1
    return customList   

def bucketSort(customList):
    numberOfBuckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    arr = []

    for i in range(numberOfBuckets):
        arr.append([])
    
    for j in customList:
        index_b = math.ceil(j * numberOfBuckets/maxValue)
        arr[index_b-1].append(j)

    for i in range(numberOfBuckets):
        arr[i] = insertionSort(arr[i])

    k = 0
    for i in range(numberOfBuckets):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1
    print(customList)

customList = [9, 7, 5, 3, 1]   
bucketSort(customList)
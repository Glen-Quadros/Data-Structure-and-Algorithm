import numpy as np

myArray = np.array([1,9,2,8,3,7,4,6,5])

def findMaxProduct(array):
    maxProduct = 0
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] * array[j] > maxProduct:
                maxProduct = array[i] * array[j]
                pairs = str(array[i]) + ' ' + str(array[j])
    print(pairs)
    print(maxProduct)

findMaxProduct(myArray)

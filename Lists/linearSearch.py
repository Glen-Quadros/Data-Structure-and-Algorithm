import numpy as np

myArray = np.array([1,2,3,4,5,6,7,8,9,10])

def linearSearch(array, target):
    for i in range(len(array)):
        if array[i] == target:
            print('Element found at ' + str(i))

linearSearch(myArray, 9)
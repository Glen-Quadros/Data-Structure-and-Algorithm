import numpy as np

twoDArray = np.array([[11, 15, 10, 6], 
                    [10, 14, 11, 5], 
                    [12, 17, 12, 8],
                    [15, 18, 14, 9]])

print(twoDArray)

# Insertion 
newTwoDArray = np.insert(twoDArray, 0, [[1,2,3,4]], axis=0)
print(newTwoDArray)

# Append
newTwoDArray1 = np.append(twoDArray, [[1,2,3,4]], axis=0)
print(newTwoDArray1)

# Accessing elements in Two-Dimensional Array 
def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]):
        print('Incorrect Index Values')
    else:
        print(array[rowIndex][colIndex])

print(accessElements(twoDArray, 2, 3))

# Traversing a two dimensional array
def traversal(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

print(traversal(twoDArray))

# Searching two dimensional array
def searchTwoDArray(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return 'Element found at ' + str(i) + ' ' + str(j)
    return 'Element not found'

print(searchTwoDArray(twoDArray, 14))

# Deletion in two dimensional array
newTDArray = np.delete(twoDArray, 0, axis=1)
print(newTDArray)
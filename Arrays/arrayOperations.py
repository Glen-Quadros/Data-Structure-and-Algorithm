from array import *

myArray = array('i', [1,2,3,4,5,6])

# To insert
myArray.insert(6, 7)
print(myArray)

# For traversal
def traversalArray(array):
    for i in array:
        print(i)
traversalArray(myArray)

# To access an element
def accessElement(array, index):
    if index >= len(array):
        print('There is no element in this index')
    else:
        print(array[index])
accessElement(myArray, 5)

# Searching for an element in the array
def searchInArray(array, value):
    for i in array:
        if i == value:
            return array.index(value)
    return 'The element does not exist in the array'
searchInArray(myArray, 3)

# Deleting an element in the array
myArray.remove(7)
print(myArray)
from array import *

# 1. Create an array and traverse.
myArray = array('i', [1,2,3,4,5,6])

for i in myArray:
    print(i)

# 2. Access individual elements through indexes
print('\n')
print(myArray[2])

# 3. Append any value to the array using append() method
print('\n')
myArray.append(7)
print(myArray)

# 4. Insert value in an array using insert() method
print('\n')
myArray.insert(7,8)
print(myArray)

# 5. Extend python array using extend() method
print('\n')
myArray1 = array('i', [9,10,11])
myArray.extend(myArray1)
print(myArray)

# 6. Add items from list into array using fromlist() method
print('\n')
tempList = [12,13,14]
myArray.fromlist(tempList)
print(myArray)

# 7. Remove any array element using remove() method
print('\n')
myArray.remove(14)
print(myArray)

# 8. Remove last array element using pop() method
print('\n')
myArray.pop(12)
print(myArray)

# 9. Fetch any element through its index using index() method
print('\n')
print(myArray.index(11))

# 10. Reverse a python array using reverse() method
print('\n')
myArray.reverse()
print(myArray)

# 11. Get array buffer information through buffer_info() method
print('\n')
print(myArray.buffer_info())

# 12. Check for number of occurrences of an element using count () method
print('\n')
print(myArray.count(1))

# 13. Convert array to a python list with same elements using tolist() method
print('\n')
print(myArray.tolist())

# 14. Slice Elements from an array
print('\n')
print(myArray[1:4])

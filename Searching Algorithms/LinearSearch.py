def linearSearch(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1
        
array = [1,2,3,4,5,6]
print(linearSearch(array, 6))
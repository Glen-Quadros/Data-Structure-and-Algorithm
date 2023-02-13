def rotateMatrix(matrix):
    n = len(matrix)
    # Transpose matrix
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Now for reversal
    for i in range(n):
        matrix[i].reverse()

myList = [[1,2,3], 
        [4,5,6], 
        [7,8,9]]
rotateMatrix(myList)
print("Rotated Image")
for i in range(len(myList)):
    for j in range(len(myList[0])):
        print(myList[i][j], end=" ")
    print()


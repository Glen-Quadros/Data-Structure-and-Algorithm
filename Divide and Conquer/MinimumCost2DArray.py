# Find minimum cost to reach the last cell in a 2D array. (You cannot travel diagonally)

def findMinimumCost(twoDArray, row, col):
    if row == -1 or col == -1:
        return float('inf')
    elif row == 0 and col == 0:
        return twoDArray[row][col]
    else:
        op1 = findMinimumCost(twoDArray, row-1, col)
        op2 = findMinimumCost(twoDArray, row, col-1)
        return (twoDArray[row][col] + min(op1, op2))
    
twoDArray = [[4, 7, 8, 6, 4],
             [6, 7, 3, 9, 2],
             [3, 8, 1, 2, 4],
             [7, 1, 7, 3, 7],
             [2, 9, 8, 9, 3]]

print(findMinimumCost(twoDArray, 4, 4))
    
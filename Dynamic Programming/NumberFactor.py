# N as the sum of 1, 3 and 4

# Top Down approach
def numberFactorTopDown(n, tempDict):
    if n in (0, 1, 2):
        return 1
    elif n == 3:
        return 2
    else:
        if n not in tempDict:
            subP1 = numberFactorTopDown(n-1, tempDict)
            subP2 = numberFactorTopDown(n-3, tempDict)
            subP3 = numberFactorTopDown(n-4, tempDict)
            tempDict[n] = subP1 + subP2 + subP3
        return tempDict[n]
    
# Bottum Up Approach
def numberFactorBU(n):
    tempArray = [1, 1, 1, 2]
    for i in range(4, n+1):
        tempArray.append(tempArray[i-1] + tempArray[i-3] + tempArray[i-4])
    return tempArray[n]
    
print(numberFactorTopDown(5, {}))
print(numberFactorBU(5))

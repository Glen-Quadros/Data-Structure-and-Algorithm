def findLSP(s, startIndex, endIndex):
    if startIndex > endIndex:
        return 0
    elif startIndex == endIndex:
        return 1
    elif s[startIndex] == s[endIndex]:
        return 2 + findLSP(s, startIndex+1, endIndex-1)
    else:
        op1 = findLSP(s, startIndex, endIndex-1)
        op2 = findLSP(s, startIndex+1, endIndex)
        return max(op1, op2)
    
print(findLSP('ELRMENMET', 0, 8))
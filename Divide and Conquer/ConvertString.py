'''
Given two strings S1 and S2, convert string S2 to S1 using minimum count of operations.
You can use insert, delete and insert operations.
'''

def findMinimumOperations(s1, s2, index1, index2):
    if index1 == len(s1):
        return len(s2) - index2
    if index2 == len(s2):
        return len(s1) - index1
    if s1[index1] == s2[index2]:
        return findMinimumOperations(s1, s2, index1+1, index2+1)
    else:
        deleteOp = 1 + findMinimumOperations(s1, s2, index1, index2+1)
        insertOp = 1 + findMinimumOperations(s1, s2, index1+1, index2)
        replaceOp = 1 + findMinimumOperations(s1, s2, index1+1, index2+1)
        return min(deleteOp, insertOp, replaceOp)

print(findMinimumOperations('table', 'tbrles', 0, 0))
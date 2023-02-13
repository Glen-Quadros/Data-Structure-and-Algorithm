myList = [1,2,3,4,6,7,8,9,10]

def findMissingNumber(myList):
    sumOfNNumbers = 10 * (10+1)/2
    sumOfmyList = sum(myList)
    if sumOfNNumbers == sumOfmyList:
        print('No elements are missing')
    else:
        missingNumber = sumOfNNumbers - sumOfmyList
        print(int(missingNumber))

findMissingNumber(myList)
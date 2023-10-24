'''
Given N houses along the street with some money, find the maximum amount that can be 
stolen given that adjacent houses cannot be stolen
'''

def houseRobber(houses, currentIndex):
    if currentIndex >= len(houses):
        return 0
    else:
        stealFirstHouse = houses[currentIndex] + houseRobber(houses, currentIndex+2)
        skipFirstHouse = houseRobber(houses, currentIndex + 1)
        
        return max(stealFirstHouse, skipFirstHouse)
    
houses = [6, 7, 1, 30, 8, 2, 4]
print(houseRobber(houses, 0))

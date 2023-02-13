list = [1,2,3,3,5,6,7,8,9]

def twoSum(list, target):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] == list[j]: 
                continue
            elif list[i] + list[j] == target:
                print(i, j)

twoSum(list, 9)
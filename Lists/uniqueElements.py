list = [1,2,3,4,5,6,7,8,9,3]

def isUnique(list):
    a = []
    for i in list:
        if i in a:
            print(i) 
            return False
        else:
            a.append(i)
    return True

print(isUnique(list))
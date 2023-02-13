shoppingList = ['Milk', 'Cheese', 'Butter']

shoppingList[2] = 'Egg'
print(shoppingList[2])

# Insert, Append and extend operations
shoppingList.insert(3, 'Meat')
print(shoppingList)

shoppingList.append('Bread')
print(shoppingList)

newList = ['Water', 'Rice']
shoppingList.extend(newList)
print(shoppingList)

# Slice Operation
print(shoppingList[:2])

# Pop, delete and remove methods
shoppingList.pop(2)
print(shoppingList)

del shoppingList[5]
print(shoppingList)

shoppingList.remove('Milk')
print(shoppingList)

#Searching in List
myList = [1,2,3,4]
if 2 in myList:
    print('Element is present')
else:
    print('Element not present')

def search(list, element):
    for i in list:
        if i == element:
            return 'Element found at ' + str(list.index(element))
    return 'Element not found'

print(search(myList, 5))
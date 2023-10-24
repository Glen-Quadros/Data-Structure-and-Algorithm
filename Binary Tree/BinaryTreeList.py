class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.maxSize = size
        self.lastUsedIndex = 0

    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return 'The binary tree is full'
        self.customList[self.lastUsedIndex + 1] = value
        self.lastUsedIndex += 1
        return 'The value has been successfully added'
    
    def searchNode(self, nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return 'Success'
        return 'Not Found'

    def preOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2 + 1)

    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.preOrderTraversal(index*2)
        print(self.customList[index])
        self.preOrderTraversal(index*2 + 1)

    def postOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2 + 1)
        print(self.customList[index])

    def levelOrderTravsersal(self, index):
        for i in range(index, self.lastUsedIndex+1):
            print(self.customList[i])
    
    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            return 'There is no node to delete'
        for i in range(1, self.lastUsedIndex+1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return 'The node has been succesfully deleted'
            
    def deleteBT(self):
       self.customList = None
       return "The BT has been successfully deleted"   
    
# newBT = BinaryTree(8)
# newBT.insertNode("Drinks")
# newBT.insertNode("Hot")
# newBT.insertNode("Cold")
# newBT.insertNode("Tea")
# newBT.insertNode("Coffee")

# print(newBT.deleteBT())

# newBT.levelOrderTraversal(1)
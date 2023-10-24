import QueueLinkedList as queue

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None
    
def insertNode(rootNode, nodeValue):
    if rootNode is None: 
        rootNode.value = nodeValue
    elif nodeValue <= rootNode.value:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)
    return 'Node has been added successfully'

def preOrderTravsersal(rootNode):
    if not rootNode:
        return
    print(rootNode.value)
    preOrderTravsersal(rootNode.leftChild)
    preOrderTravsersal(rootNode.rightChild)

def inOrderTravsersal(rootNode):
    if not rootNode:
        return
    preOrderTravsersal(rootNode.leftChild)
    print(rootNode.value)
    preOrderTravsersal(rootNode.rightChild)

def postOrderTravsersal(rootNode):
    if not rootNode:
        return
    preOrderTravsersal(rootNode.leftChild)
    preOrderTravsersal(rootNode.rightChild)
    print(rootNode.value)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.value)
            if rootNode.value.leftChild is not None:
                customQueue.enqueue(rootNode.value.leftChild)
            if rootNode.value.rightChild is not None:
                customQueue.enqueue(rootNode.value.rightChild)

def searchNode(rootNode, nodeValue):
    if rootNode.value == nodeValue:
        print('The value is found')
    elif nodeValue < rootNode.value:
        if rootNode.leftChild.value == nodeValue:
            print('The value is found')
        else:
            searchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild.value == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.rightChild, nodeValue)

def minValueNode(bstNode):
    current = bstNode
    while current.leftChild is not None:
        current = current.leftChild
    return current

def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        
        temp = minValueNode(rootNode.rightChild)
        rootNode.data = temp.data 
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    return rootNode

def deleteBST(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The BST has been successfully deleted"



newBST = BSTNode(None)
insertNode(newBST, 70)
insertNode(newBST,50)
insertNode(newBST,90)
insertNode(newBST, 30)
insertNode(newBST,60)
insertNode(newBST,80)
insertNode(newBST,100)
insertNode(newBST,20)
insertNode(newBST,40)
print(deleteBST(newBST))
levelOrderTraversal(newBST)
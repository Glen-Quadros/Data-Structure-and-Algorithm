class Heap:
    def __init__(self, size):
        self.customList = (size+1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1

def peekHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.customList[1]
    
def sizeOfHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapSize

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1, rootNode.heapSize+1):
            print(rootNode.customList[i])

def heapifyTreeInsert(rootNode, index, heapType):
    parentIndex = int(index/2)
    if index <= 1:
        return 
    if heapType == 'Min':
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)
    elif heapType == 'Max':
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)

def insertNode(rootNode, nodeValue, heapType):
    if rootNode.heapSize+1 == rootNode.maxSize:
        return 'The Binary Heap is full'
    rootNode.customList[rootNode.heapSize + 1] = nodeValue
    rootNode.heapSize += 1
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
    return "The value has been successfully inserted"

def heapifyTreeExtract(rootNode, index, heapType):
    leftIndex = index * 2
    rightIndex = index * 2 + 1
    swapChild = 0

    if rootNode.index < leftIndex:
        return
    elif rootNode.heapSize == leftIndex:
        if heapType == 'Min':
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return 
        elif heapType == 'Max':
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
    elif rootNode.customList[index] > leftIndex:
        if heapType == 'Min':
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        elif heapType == 'Max':
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        heapifyTreeExtract(rootNode, swapChild, heapType)

def extractNode(rootNode, index, heapType):
    if rootNode.heapSize == 0:
        return 
    else:
        extractedNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -= 1
        heapifyTreeExtract(rootNode, 1, heapType)
        return extractedNode

def deleteEntireBinaryHeap(rootNode):
    rootNode.customList = None
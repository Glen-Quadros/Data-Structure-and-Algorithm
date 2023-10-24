class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
    
    def createCDLL(self, nodeValue):
        newNode = Node(nodeValue)
        self.head = newNode
        self.tail = newNode
        newNode.prev = newNode
        newNode.next = newNode

    def insertCDLL(self, nodeValue, location):
        if self.head is None:
            return 'Circular Doubly Linked List is empty'
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                tempNode.next.prev = newNode
                tempNode.next = newNode
    
    def traversalCDLL(self):
        if self.head is None:
            print('Empty Circular Doubly Linked list')
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                if tempNode == self.tail:
                    break
                tempNode = tempNode.next

    def reverseTraversalCDLL(self):
        if self.head is None:
            print('Empty Circular Doubly Linked list')
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                if tempNode == self.head:
                    break
                tempNode = tempNode.prev

    def searchCDLL(self, nodeValue):
        if self.head is None:
            print('Empty Circular Doubly Linked list')
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                if tempNode == self.tail:
                    break
                tempNode = tempNode.next
    
    def deleteNode(self, location):
        if self.head is None:
            print('No node to delete')
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                currNode = self.head
                index = 0
                while index < location - 1:
                    currNode = currNode.next
                    index = index + 1
                currNode.next = currNode.next.next
                currNode.next.prev = currNode
    
    def deleteCDLL(self):
        if self.head is None:
            print('No CDLL to delete')
        else:
            self.tail.next = None
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None 

cdll = CircularDoublyLinkedList()
cdll.createCDLL(0)
cdll.insertCDLL(2, -1)
cdll.insertCDLL(3,1)
cdll.traversalCDLL()
cdll.reverseTraversalCDLL()
print(cdll.searchCDLL(0))
cdll.deleteNode(0)
cdll.deleteCDLL()
print([node.value for node in cdll])
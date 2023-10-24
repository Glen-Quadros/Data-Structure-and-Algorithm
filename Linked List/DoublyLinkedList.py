class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def createDLL(self, nodeValue):
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node

    def insertDLL(self, nodeValue, location):
        if self.head is None:
            print('The doubly linked list is empty')
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == -1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index = index + 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode
    
    def traversalDLL(self):
        if self.head is None:
            print('The doubly linked list is empty')
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
    
    def reverseTraversal(self):
        if self.head is None:
            print('The doubly linked list is empty')
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev
    
    def searchDLL(self, nodeValue):
        if self.head is None:
            print('The doubly linked list is empty')
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
            return 'The node does not exist in the doubly linked list'
        
    def deleteNode(self, location):
        if self.head is None:
            print('The doubly linked list is empty')
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                currNode = self.head
                index = 0
                while index < location - 1:
                    currNode = currNode.next
                    index = index + 1
                currNode.next = currNode.next.next
                currNode.next.prev = currNode 

    def deleteDLL(self):
        if self.head is None:
            print('The doubly linked list is empty')
        else:
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None

dll = DoublyLinkedList()
dll.createDLL(0)
dll.insertDLL(3,-1)
dll.insertDLL(1,1)
dll.insertDLL(2,2)
dll.traversalDLL()
dll.reverseTraversal()
print(dll.searchDLL(3))
dll.deleteNode(0)
dll.deleteDLL()
print([node.value for node in dll])
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next
    
    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node

    def insertCSLL(self, value, location):
        if self.head is None:
            print('The linked list is empty')
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index = index + 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = tempNode

    def traversalCSLL(self):
        if self.head is None:
            print('The linked list is empty')        
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break

    def searchCSLL(self, nodeValue):
        if self.head is None:
            return 'Linked list does not exist'
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    return 'Element not found in Circular Linked List'
    
    def deleteNode(self, location):
        if self.head is None:
            print('The node is empty')
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index = index + 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    def deleteCSLL(self):
        self.head = None
        self.tail.next = None
        self.tail = None

csll = CircularSinglyLinkedList()
csll.createCSLL(0)
csll.insertCSLL(1,0)
csll.insertCSLL(3,-1)
csll.insertCSLL(2,0)
csll.traversalCSLL()
print(csll.searchCSLL(0))
csll.deleteNode(0)
csll.deleteCSLL()
print([node.value for node in csll])


                        
                        
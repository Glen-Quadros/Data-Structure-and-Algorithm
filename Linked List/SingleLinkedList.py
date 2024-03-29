class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield(node)
            node = node.next

    def insertSingleLinkedList(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                newNode.next = None
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
                newNode.next = nextNode

    def traverseSingleLinkedList(self):
        if self.head is None:
            print('The single Linked List is empty')
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    def searchSingleLinkedList(self,nodeValue):
        if self.head is None:
            print('The linked list is empty')
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return 'The value is not present in the Linked List'
        
    def deletingNodeLinkedList(self, location):
        if self.head is None:
            print('The linked list is empty')
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:                    
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index = index + 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    def deleteEntireSingleLinkedList(self):
        if self.head is None:
            print('The linked list does not exist')
        else:
            self.head = None
            self.tail = None

singlyLinkedList = SLinkedList()
singlyLinkedList.insertSingleLinkedList(3, 1)
singlyLinkedList.insertSingleLinkedList(2, 0)
singlyLinkedList.insertSingleLinkedList(1, -1)
singlyLinkedList.traverseSingleLinkedList()
print(singlyLinkedList.searchSingleLinkedList(5))
singlyLinkedList.deletingNodeLinkedList(-1)
singlyLinkedList.deleteEntireSingleLinkedList()
print([node.value for node in singlyLinkedList])



class Node:
    def __init__(self, value):
        self.value = value
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        currNode = self.head
        while currNode:
            yield(currNode)
            currNode = currNode.next
    
class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)

    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False
    
    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node
    
    def pop(self):
        if self.isEmpty():
            return 'No element in the stack'
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue
        
    def pop(self):
        if self.isEmpty():
            return 'No element in the stack'
        else:
            nodeValue = self.LinkedList.head.value
            return nodeValue
        
    def delete(self):
        self.LinkedList.head = None

customStack = Stack()
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
print(customStack)
print(customStack.isEmpty())
from LinkedList import LinkedList

def removeDuplicate(ll):
    if ll.head is None:
        return
    else:
        currentNode = ll.head
        visitedNodes = set([currentNode.value])
        while currentNode.next:
            if currentNode.next.value in visitedNodes:
                currentNode.next = currentNode.next.next
            else:
                visitedNodes.add(currentNode.next.value)
                currentNode = currentNode.next
        return ll
    
def removeDulicateWithoutSets(ll):
    if ll.head is None:
        return
    else:
        currentNode = ll.head
        while currentNode:
            runner = currentNode
            while runner.next:
                if runner.next.value == currentNode.value:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            currentNode = currentNode.next
        return ll
    
customll = LinkedList()
customll.generate(10,0,99)
print(customll)
print(removeDuplicate(customll))
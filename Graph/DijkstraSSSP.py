class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addNode(self, node):
        if node not in self.gdict:
            self.gdict[node] = {}
        
    def addEdge(self, fromNode, toNode, weight):
        self.gdict[fromNode][toNode] = weight

class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if self.queue:
            return self.queue.pop(0)
        return None
    
def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.gdict.keys())
    queue = Queue()
    queue.push(initial)

    while nodes:
        minNode = None
        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode = node
                elif visited[node] < visited[minNode]:
                    minNode = node
        if minNode is None:
            break

        nodes.remove(minNode)
        currentWeight = visited[minNode]

        for edge in graph.gdict[minNode]:
            weight = currentWeight + graph.gdict[minNode][edge]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = minNode
                queue.push(edge)
    
    return visited, path

customGraph = Graph()
customGraph.addNode("A")
customGraph.addNode("B")
customGraph.addNode("C")
customGraph.addNode("D")
customGraph.addNode("E")
customGraph.addNode("F")
customGraph.addNode("G")

customGraph.addEdge("A", "B", 2)
customGraph.addEdge("A", "C", 5)
customGraph.addEdge("B", "C", 6)
customGraph.addEdge("B", "D", 1)
customGraph.addEdge("B", "E", 3)
customGraph.addEdge("C", "F", 8)
customGraph.addEdge("D", "E", 4)
customGraph.addEdge("E", "G", 9)
customGraph.addEdge("F", "G", 7)

result = dijkstra(customGraph, "A")
print(result)
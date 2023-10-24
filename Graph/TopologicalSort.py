class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addEdge(self, vertex, edge):
        if vertex not in self.gdict:
            self.gdict[vertex] = []
        if edge not in self.gdict:
            self.gdict[edge] = []
        self.gdict[vertex].append(edge)

    def topologicalSortUtil(self, v, visited, stack):
        visited.append(v)

        for i in self.gdict[v]:
            if i not in visited:
                self.topologicalSortUtil(i, visited, stack)
        
        stack.insert(0, v)

    def topologicalSort(self):
        visited = []
        stack = []

        for k in list(self.gdict):
            if k not in visited:
                self.topologicalSortUtil(k, visited, stack)
        
        print(stack)

customGraph = Graph()
customGraph.addEdge("A", "C")
customGraph.addEdge("C", "E")
customGraph.addEdge("E", "H")
customGraph.addEdge("E", "F")
customGraph.addEdge("F", "G")
customGraph.addEdge("B", "D")
customGraph.addEdge("B", "C")
customGraph.addEdge("D", "F")

customGraph.topologicalSort()
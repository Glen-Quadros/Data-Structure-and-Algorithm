class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.nodes = []

    def addEdges(self, s, d, w):
        self.graph.append([s, d, w])
    
    def addNode(self, value):
        self.nodes.append(value)

    def printSolution(self, distance):
        print('Vertex Distance from source')
        for key, value in distance.items():
            print(' ' + key + ' :  ', value)
        
    def bellmanFord(self, src):
        distance = {i : float('Inf') for i in self.nodes}
        distance[src] = 0

        for _ in range(self.V - 1):
            for s, d, w in self.graph:
                if distance != float('Inf') and distance[s] + w < distance[d]:
                    distance[d] = distance[s] + w
            
        for s, d, w in self.graph:
            if distance != float('Inf') and distance[s] + w < distance[d]:
                print('Graph contains negative cycle')
                return 
        
        self.printSolution(distance)

g = Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.addEdges("A", "C", 6)
g.addEdges("A", "D", 6)
g.addEdges("B", "A", 3)
g.addEdges("C", "D", 1)
g.addEdges("D", "C", 2)
g.addEdges("D", "B", 1)
g.addEdges("E", "B", 4)
g.addEdges("E", "D", 2)
g.bellmanFord("E")
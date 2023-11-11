class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = [[inf] * n for _ in range(n)]
        for fromNode, toNode, edgeCost in edges:
            self.graph[fromNode][toNode] = edgeCost
        
        for i in range(n):
            self.graph[i][i] = 0
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    self.graph[i][j] = min(self.graph[i][j], self.graph[i][k] + self.graph[k][j])

    def addEdge(self, edge: List[int]) -> None:
        n = len(self.graph)
        fromNode, toNode, costEdge = edge
        for i in range(n):
            for j in range(n):
                self.graph[i][j] = min(self.graph[i][j], self.graph[i][fromNode] + self.graph[toNode][j] + costEdge)

    def shortestPath(self, node1: int, node2: int) -> int:
        if self.graph[node1][node2] == inf:
            return -1
        
        return self.graph[node1][node2]

        

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
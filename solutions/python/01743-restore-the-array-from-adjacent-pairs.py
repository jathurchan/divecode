class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u,v in adjacentPairs: # build the graph
            graph[u].append(v)
            graph[v].append(u)
        
        startNode = None

        for node in graph.keys():
            if len(graph[node]) == 1:
                startNode = node
                break
        
        ans = []
        curr, seen = startNode, set()
        while curr is not None:
            ans.append(curr)
            seen.add(curr)
            candidates = graph[curr]
            curr = None
            for nextNode in candidates:
                if nextNode not in seen:
                    curr = nextNode
        
        return ans
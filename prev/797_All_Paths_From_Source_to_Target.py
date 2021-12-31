class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        
        n = len(graph)
        
        result = []
        
        def explore(curr, path):
            
            if curr == n-1:
                result.append(path + [n-1])
                return
            
            for nxt in graph[curr]:
                explore(nxt, path + [curr])
        
        explore(0, [])
        
        return result

# Runtime: 84 ms, faster than 90.46% of Python online submissions for All Paths From Source to Target.
# Memory Usage: 14.9 MB, less than 49.82% of Python online submissions for All Paths From Source to Target.
class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        
        n = len(arr)
        
        visited = [False]*n
        
        def DFS(i):
            
            if i >= n or i < 0: # Out of bounds?
                return False
            
            if visited[i]:  # already visited => not this way
                return False
            
            if arr[i] == 0: # canReach !
                return True
            
            visited[i] = True
            
            return DFS(i + arr[i]) or DFS(i - arr[i])
        
        return DFS(start)
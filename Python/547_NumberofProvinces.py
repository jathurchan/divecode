class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        
        n = len(isConnected)
        
        visited = [False]*n
        count = 0
        
        def dfs(idx):
            for j in range(n):
                if isConnected[idx][j] == 1 and not visited[j]:
                    visited[j] = True
                    dfs(j)
        
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1
        
        return count
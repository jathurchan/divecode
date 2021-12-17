class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        maxSideLen = 0
        
        m, n = len(matrix), len(matrix[0])
        
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(min(dp[i][j-1], dp[i-1][j-1]), dp[i-1][j]) + 1
                    maxSideLen = max(dp[i][j], maxSideLen)
                    
        return maxSideLen * maxSideLen
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 1:  # null or single node BST
            return 1
        
        dp = [0]* (n+1) # array that stores the values for each k between 0 and n (Dynamic Programming)

        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            for k in range(0, i//2):
                dp[i] += dp[k] * dp[i-1-k]
            dp[i] *= 2

            if (i % 2 == 1):    # Do not forget i/2 if i is odd
                dp[i] += dp[i//2] * dp[i//2]
        
        return dp[n]

sol = Solution()
print(sol.numTrees(3))
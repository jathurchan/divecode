class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [0] * (n+1)

        square_nums = [i*i for i in range(1, int(math.sqrt(n) + 1))]
        
        dp = [float('inf')] * (n+1)
        
        dp[0] = 0
        
        for i in range(1, n+1):
            for square in square_nums:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i-square]+1)
        return dp[-1]
        
        # ---- TIME LIMIT EXCEEDED ----
        #  # find all perfect squares below n
        
        # perf_squares = []
        # k = 1
        # while k*k < n:
        #     perf_squares.append(k*k)
        #     k += 1
        
        # # recursion
        
        # def determine_min(r):
        #     if r in perf_squares:
        #         return 1
            
        #     min_r = float('inf')
            
        #     for sq in perf_squares:
        #         if r < sq:
        #             break
        #         new_r = determine_min(r-sq) + 1
        #         min_r = min(min_r, new_r)
        #     return min_r
        
        # return determine_min(n)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost)+1)    # dp[-1] = top of the floor
        
        for i in range(2, len(cost)+1): # can start from 0 or 1
            dp[i] = min(dp[i-2]+ cost[i-2], dp[i-1] + cost[i-1])
        
        return dp[-1]
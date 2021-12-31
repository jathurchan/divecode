class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        n = len(prices)

        if n < 2:
            return 0    # No profit
        
        profit = 0

        for i in range(1, n):
            if prices[i] > prices[i-1]:     # we can buy and sell on the same day
                profit += (prices[i] - prices[i-1])
        
        return profit
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        temp = 1
        
        while temp < n:
            temp *= 3
        
        return temp == n
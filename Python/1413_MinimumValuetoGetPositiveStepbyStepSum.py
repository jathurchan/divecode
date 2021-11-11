class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        minSum = 0
        sum = 0

        for n in nums:
            sum += n
            if sum < minSum:
                minSum = sum
        
        return minSum * -1 + 1
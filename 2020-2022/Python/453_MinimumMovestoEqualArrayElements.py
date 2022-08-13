class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        
        n, count = len(nums), 0
        
        for i in range(n-1, -1, -1):
            count += nums[i] - nums[0]
        
        return count
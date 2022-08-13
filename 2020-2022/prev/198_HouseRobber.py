class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        
        e = 0
        o = 0
        
        for i in range(n):
            if i % 2 == 0:
                e = max(e + nums[i], o)
            else:
                o = max(o + nums[i], e)
        
        return max(e, o)
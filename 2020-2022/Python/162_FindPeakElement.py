class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        
        for i in range(n-1):
            if nums[i+1] < nums[i]:
                return i
        
        return n-1
    
    def findPeakElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        l, r = 0, n-1

        while l < r:

            m = (l+r) // 2

            if nums[m] > nums[m+1]:
                r = m
            else:
                l = m + 1
        
        return l

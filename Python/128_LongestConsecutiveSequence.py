class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        numbersPresent = set(nums);
        
        maxLen = 0
        
        for start in nums:
            if start-1 not in nums:
                last = start + 1
                while last in nums:
                    last += 1
                if last-start > maxLen:
                    maxLen = last-start
        
        return maxLen
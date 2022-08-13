class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        nums.sort()
        
        i, j = 0, 1
        
        count = 0
        
        while (i < len(nums)) and (j < len(nums)):
            
            if i == j or nums[j] - nums[i] < k:
                j += 1
            elif nums[j] - nums[i] > k:
                i += 1
            else:
                i += 1
                count += 1
                while (i < len(nums) and nums[i] == nums[i-1]):
                    i += 1
        return count
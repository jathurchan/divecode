class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        hashmap = {}
        
        for i in range(len(nums)):
            hashmap[nums[i]] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            
            if diff in hashmap and hashmap[diff] != i:
                return [i, hashmap[diff]]
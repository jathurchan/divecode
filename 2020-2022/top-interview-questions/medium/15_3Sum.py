class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []
        nums.sort()
        
        def twoSum(ns, ix, rs):
            lo, hi = i+1, len(ns)-1
            
            while (lo < hi):
                tSum = ns[ix] + ns[lo] + ns[hi]
                if tSum < 0:
                    lo += 1
                elif tSum > 0:
                    hi -= 1
                else:   # new solution found
                    rs.append([ns[ix], ns[lo], ns[hi]])
                    lo += 1
                    hi -= 1
                    while lo < hi and ns[lo] == ns[lo-1]:
                        lo += 1
        
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                twoSum(nums, i, res)
        
        return res
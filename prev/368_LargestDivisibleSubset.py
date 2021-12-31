class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        s_nums = sorted(nums)   # sorted array

        subsets = [[num] for num in s_nums]

        for i in range(len(s_nums)):
            for j in range(i):
                if s_nums[i] % s_nums[j] == 0 and len(subsets[i]) < len(subsets[j]) + 1:
                    subsets[i] = subsets[j] + [s_nums[i]]
        
        return max(subsets, key=len)
                

sol = Solution()
print(sol.largestDivisibleSubset([5,9,18,54,108,540,90,180,360,720]))




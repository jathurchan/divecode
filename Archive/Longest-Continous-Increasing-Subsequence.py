class Solution(object):
    """
    674. Longest Continuous Increasing Subsequence

    Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence
    (i.e. subarray). The subsequence must be strictly increasing.
    A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is
    [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].
    """

    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxLength = 1
        i, n = 0, len(nums)

        while i < n:

            counter = 0
            while i + counter < n-1 and nums[i + counter] < nums[i + counter + 1]:
                counter += 1
            
            if counter + 1 > maxLength:     # update maxLength
                maxLength = counter + 1
            
            i += counter + 1    # update i

        return maxLength

sol = Solution()
print(sol.findLengthOfLCIS([1,3,5,4,7]))
print(sol.findLengthOfLCIS([2,2,2,2,2]))


        
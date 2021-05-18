class Solution(object):
    """
    1498. Number of Subsequences That Satisfy the Given Sum Condition

    Given an array of integers nums and an integer target.

    Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element
    on it is less or equal to target. Since the answer may be too large, return it modulo 109 + 7.

    Constraints:

        -   1 <= nums.length <= 105
        -   1 <= nums[i] <= 106
        -   1 <= target <= 106
    """

    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums = sorted(nums)
        n = len(nums)

        mod = 10**9 + 7
        ans = 0

        i, j = 0, n-1

        while i <= j:
            if nums[i] + nums[j] > target:
                j -= 1
            else:
                ans = (ans + 2 ** (j-i)) % mod
                i += 1
        
        return ans % mod

        


sol = Solution()
print(sol.numSubseq([2,3,3,4,6,7], 12))
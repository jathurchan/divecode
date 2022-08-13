class Solution(object):
    """
        136. Single Number

        Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
        You must implement a solution with a linear runtime complexity and use only constant extra space.

        Constraints:

            -   1 <= nums.length <= 3 * 104
            -   -3 * 104 <= nums[i] <= 3 * 104
            -   Each element in the array appears twice except for one element which appears only once.
    """
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # XOR operator ^ is commutative.
        # 1 ^ 2 = 3 but 1 ^ 2 ^ 1 = (1 ^ 1) ^ 2 = 0 ^ 2 = 2

        res = 0

        for num in nums:
            res ^= num
        
        return res

sol = Solution()
print(sol.singleNumber([2,2,1]))
        
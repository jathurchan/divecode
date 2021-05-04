class Solution(object):
    """
    287. Find the Duplicate Number

    Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
    There is only one repeated number in nums, return this repeated number.

    Constraints:

        -   2 <= n <= 105
        -   nums.length == n + 1
        -   1 <= nums[i] <= n
        -   All the integers in nums appear only once except for precisely one integer which appears two or more times.
    """

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        has_appeared = set()

        n = len(nums) - 1

        for i in range(n+1):

            if nums[i] in has_appeared:
                return nums[i]
            else:
                has_appeared.add(nums[i])
        
        return

sol = Solution()
print(sol.findDuplicate([1,3,4,2,2]))
        

        
class Solution(object):
    """
    1365. How Many Numbers Are Smaller Than the Current Number

    Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
    That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
    Return the answer in an array.

    Constraints:
        -   2 <= nums.length <= 500
        -   0 <= nums[i] <= 100
    """

    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        sorted_nums = sorted(nums)

        nOfSmallerNums = {}

        for i in range(n):
            if sorted_nums[i] not in nOfSmallerNums:
                nOfSmallerNums[sorted_nums[i]] = i

        res = []
        for i in range(n):
            res.append(nOfSmallerNums[nums[i]])

        return res

sol = Solution()
print(sol.smallerNumbersThanCurrent([6,5,4,8]))
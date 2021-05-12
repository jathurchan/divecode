class Solution(object):
    """
    442. Find All Duplicates in an Array

    Given an integer array nums of length n where all the integers of nums are in the range [1, n] and
    each integer appears once or twice, return an array of all the integers that appears twice.

    Constraints:

        -   n == nums.length
        -   1 <= n <= 105
        -   1 <= nums[i] <= n
        -   Each element in nums appears once or twice.
    """

    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        appearedNum = set()

        res = []

        for number in nums:
            if number in appearedNum:
                res.append(number)
            else:
                appearedNum.add(number)

        return res

sol = Solution()
print(sol.findDuplicates([4,3,2,7,8,2,3,1]))
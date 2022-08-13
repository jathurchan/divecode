# 523. K-diff Pairs in an Array

# Description

Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

0 <= i < j < nums.length

|nums[i] - nums[j]| == k

Notice that |val| denotes the absolute value of val.

Example 1:

Input: nums = [3,1,4,1,5], k = 2

Output: 2

Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).

Although we have two 1s in the input, we should only return the number of unique pairs.

Example 2:

Input: nums = [1,2,3,4,5], k = 1

Output: 4

Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

Example 3:

Input: nums = [1,3,1,5,4], k = 0

Output: 1

Explanation: There is one 0-diff pair in the array, (1, 1).

Constraints:

1 <= nums.length <= 104

\-107 <= nums[i] <= 107

0 <= k <= 107

## Solution

Runtime: 72 ms, faster than 42.73% of Python online submissions for K-diff Pairs in an Array.

Memory Usage: 14.5 MB, less than 96.58% of Python online submissions for K-diff Pairs in an Array.

```python
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
```


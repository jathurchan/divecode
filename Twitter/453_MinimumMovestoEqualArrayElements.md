# 453. Minimum Moves to Equal Array Elements

## Description

Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment n - 1 elements of the array by 1.

Example 1:

Input: nums = [1,2,3]

Output: 3

Explanation: Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

Example 2:

Input: nums = [1,1,1]

Output: 0

Constraints:

n == nums.length

1 <= nums.length <= 105

\-109 <= nums[i] <= 109

The answer is guaranteed to fit in a 32-bit integer.

## Thoughts

- Compute the mean and store floor of mean as the target to reach
- Get the max distance between the floor of the mean and the nunbers in the array nums

## Solution

Runtime: 236 ms, faster than 37.58% of Python online submissions for Minimum Moves to Equal Array Elements.

Memory Usage: 14.5 MB, less than 51.68% of Python online submissions for Minimum Moves to Equal Array Elements.

```python
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        
        n, count = len(nums), 0
        
        for i in range(n-1, -1, -1):
            count += nums[i] - nums[0]
        
        return count
```


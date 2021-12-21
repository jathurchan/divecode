# 78. Subsets

## Description

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]

Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]

Output: [[],[0]]

Constraints:

1 <= nums.length <= 10

\-10 <= nums[i] <= 10

All the numbers of nums are unique.

## Solution

Runtime: 16 ms, faster than 94.70% of Python online submissions for Subsets.

Memory Usage: 13.7 MB, less than 19.37% of Python online submissions for Subsets.

```python
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        n = len(nums)
        
        output = []
        
        def backtrack(index, acc):
            if index == n:
                output.append(acc[:])
                return
            
            backtrack(index+1, acc + [nums[index]])
            
            backtrack(index+1, acc)
        
        backtrack(0, [])
        return output
```


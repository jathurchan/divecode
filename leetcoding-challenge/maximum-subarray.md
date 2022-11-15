---
date: 2022.11.15
title: 53. Maximum Subarray
difficulty:
    - medium
runtime: 98.60 # faster than (in %)
memory usage: 11.36    # less than (in %)
---
## Description
Given an integer array `nums`, find the subarray which has the largest sum and return *its sum*.

**Example 1:**

```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

```

**Example 2:**

```
Input: nums = [1]
Output: 1

```

**Example 3:**

```
Input: nums = [5,4,-1,7,8]
Output: 23

```

**Constraints:**

- `1 <= nums.length <= 105`
- `104 <= nums[i] <= 104`

**Follow up:** If you have figured out the `O(n)` solution, try coding another solution using the **divide and conquer** approach, which is more subtle.

## Approach 1: if current sum becomes negative, ignore everything before
Time complexity: `O(n)`    |    Space complexity: `O(1)`
where `n` is the length of nums

``` python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        maxSum, currSum = -float('inf'), 0
        
        for j in range(n):
            currSum += nums[j]
            
            if currSum > maxSum:
                maxSum = currSum
            
            if currSum < 0:
                currSum = 0
        
        return maxSum
```
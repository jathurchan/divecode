---
date: 2022.11.15
title: Running Sum of 1d Array
difficulty:
    - easy
runtime: 93.87 # faster than (in %)
memory usage: 73.06    # less than (in %)
---
## Description
Given an array `nums`. We define a running sum of an array as `runningSum[i] = sum(nums[0]…nums[i])`.

Return the running sum of `nums`.

**Example 1:**

```
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
```

**Example 2:**

```
Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
```

**Example 3:**

```
Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]

```

**Constraints:**

- `1 <= nums.length <= 1000`
- `10^6 <= nums[i] <= 10^6`

## Approach 1: Prefix sum
Time complexity: `O(n)`    |    Space complexity: `O(n)`


``` python
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        
        for j in range(1, len(nums)):
            prefix.append(nums[j] + prefix[-1])
        
        return prefix
```
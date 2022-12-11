---
date: 2022.11.15
title: 643. Maximum Average Subarray I
difficulty:
    - easy
runtime: 19.57 # faster than (in %)
memory usage: 15.81    # less than (in %)
---
## Description
You are given an integer array `nums` consisting of `n` elements, and an integer `k`.

Find a contiguous subarray whose **length is equal to** `k` that has the maximum average value and return *this value*. Any answer with a calculation error less than `10-5` will be accepted.

**Example 1:**

```
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

```

**Example 2:**

```
Input: nums = [5], k = 1
Output: 5.00000

```

**Constraints:**

- `n == nums.length`
- `1 <= k <= n <= 105`
- `104 <= nums[i] <= 104`

## Approach 1: Sliding window
Time complexity: `O(n)`    |    Space complexity: `O(1)`


``` python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        i, curr = 0, 0
        
        for j in range(k):
            curr += nums[j]
        
        maxSum = curr
        
        while i+k < n:
            curr -= nums[i]
            curr += nums[i+k]
            
            if curr > maxSum:
                maxSum = curr
            
            i += 1
        
        return maxSum / k
```
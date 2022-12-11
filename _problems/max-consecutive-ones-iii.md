---
date: 2022.11.15
title: 1004. Max Consecutive Ones III
difficulty:
    - medium
runtime: 38.84 # faster than (in %)
memory usage: 21.13    # less than (in %)
---
## Description
Given a binary array `nums` and an integer `k`, return *the maximum number of consecutive* `1`*'s in the array if you can flip at most* `k` `0`'s.

**Example 1:**

```
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
```

**Example 2:**

```
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

```

**Constraints:**

- `1 <= nums.length <= 105`
- `nums[i]` is either `0` or `1`.
- `0 <= k <= nums.length`

## Approach 1: Sliding window
Time complexity: `O(n)`    |    Space complexity: `O(1)`
where `n` is the length of `nums`

``` python
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        
        remFlips = k
        
        for right in range(n):
            
            remFlips -= 1 - nums[right]
            
            if remFlips < 0:
                remFlips += 1 - nums[left]
                left += 1
            
        return right - left + 1
```
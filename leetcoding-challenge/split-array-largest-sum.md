---
date: 2022.11.19
title: 410. Split Array Largest Sum
difficulty:
    - hard
runtime: 51.25 # faster than (in %)
memory usage: 40.47    # less than (in %)
---
## Description
Given an integer array `nums` and an integer `k`, split `nums` into `k` non-empty subarrays such that the largest sum of any subarray is **minimized**.

Return *the minimized largest sum of the split*.

A **subarray** is a contiguous part of the array.

**Example 1:**

```
Input: nums = [7,2,5,10,8], k = 2
Output: 18
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.

```

**Example 2:**

```
Input: nums = [1,2,3,4,5], k = 2
Output: 9
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.

```

**Constraints:**

- `1 <= nums.length <= 1000`
- `0 <= nums[i] <= 106`
- `1 <= k <= min(50, nums.length)`

## Approach 1: Binary search
Time complexity: `O(n+log(s))`    |    Space complexity: `O(1)`
where `n` is the length of `nums` and `s` the sum of `nums`

``` python
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def min_subarrays_required(max_sum_allowed):
            curr_sum = 0
            splits_required = 0
            
            for element in nums:
                if curr_sum + element <= max_sum_allowed:
                    curr_sum += element
                else:
                    curr_sum = element
                    splits_required += 1
            
            return splits_required + 1
        
        left = max(nums)
        right = sum(nums)
        
        while left <= right:
            max_sum_allowed = (left + right) // 2
            
            if min_subarrays_required(max_sum_allowed) <= k:
                right = max_sum_allowed - 1
                minimum_largest_split_sum = max_sum_allowed
            else:
                left = max_sum_allowed + 1
        
        return minimum_largest_split_sum
```
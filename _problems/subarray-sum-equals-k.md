---
date: 2022.11.15
title: 560. Subarray Sum Equals K
difficulty:
    - medium
runtime: 57.79 # faster than (in %)
memory usage: 8.42    # less than (in %)
---
## Description
Given an array of integers `nums` and an integer `k`, return *the total number of subarrays whose sum equals to* `k`.

A subarray is a contiguous **non-empty** sequence of elements within an array.

**Example 1:**

```
Input: nums = [1,1,1], k = 2
Output: 2

```

**Example 2:**

```
Input: nums = [1,2,3], k = 3
Output: 2

```

**Constraints:**

- `1 <= nums.length <= 2 * 104`
- `1000 <= nums[i] <= 1000`
- `107 <= k <= 107`

## Approach 1: Count number of subarrays with exact constraint
Time complexity: `O(n)`    |    Space complexity: `O(n)`
where `n` is the length of `nums`

``` python
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        curr = 0
        res = 0
        
        for num in nums:
            curr += num
            res += counts[curr-k]
            counts[curr] += 1
        
        return res
```
---
date: 2022.11.16
title: 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
difficulty:
    - medium
runtime: 80.28 # faster than (in %)
memory usage: 74.88    # less than (in %)
---
## Description
Given an array of integers `nums` and an integer `limit`, return the size of the longest **non-empty** subarray such that the absolute difference between any two elements of this subarray is less than or equal to `limit`*.*

**Example 1:**

```
Input: nums = [8,2,4,7], limit = 4
Output: 2
Explanation: All subarrays are:
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4.
Therefore, the size of the longest subarray is 2.

```

**Example 2:**

```
Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.

```

**Example 3:**

```
Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3

```

**Constraints:**

- `1 <= nums.length <= 105`
- `1 <= nums[i] <= 109`
- `0 <= limit <= 109`

## Approach 1: Using 2 deques (increasing and decreasing)
Time complexity: `O(n)`    |    Space complexity: `O(n)`
where `n` is the length of `nums`

``` python
from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        n = len(nums)
        
        i = 0
        
        incr_idx = deque()    # store min in the sliding window
        decr_idx = deque()    # store max in the sliding window
        
        max_size = 0
        
        for j in range(n):
            
            while incr_idx and nums[incr_idx[-1]] > nums[j]:
                incr_idx.pop()
            
            incr_idx.append(j)
            
            while decr_idx and nums[decr_idx[-1]] < nums[j]:
                decr_idx.pop()
            
            decr_idx.append(j)
            
            while i < j and nums[decr_idx[0]] - nums[incr_idx[0]] > limit:
                
                if incr_idx[0] == i:
                    incr_idx.popleft()
                if decr_idx[0] == i:
                    decr_idx.popleft()
                    
                i += 1
            
            max_size = max(max_size, j - i + 1)
        
        return max_size
```
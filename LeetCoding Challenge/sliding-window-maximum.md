---
date: 2022.11.16
title: 239. Sliding Window Maximum
difficulty:
    - hard
runtime: 78.51 # faster than (in %)
memory usage: 94.51    # less than (in %)
---
## Description
You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return *the max sliding window*.

**Example 1:**

```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  73
 1 [3  -1  -3] 5  3  6  73
 1  3 [-1  -3  5] 3  6  7 5
 1  3  -1 [-3  5  3] 6  75
 1  3  -1  -3 [5  3  6] 76
 1  3  -1  -3  5 [3  6  7]7
```

**Example 2:**

```
Input: nums = [1], k = 1
Output: [1]

```

**Constraints:**

- `1 <= nums.length <= 105`
- `104 <= nums[i] <= 104`
- `1 <= k <= nums.length`

## Approach 1: Monotonous decreasing deque
Time complexity: `O(n)`    |    Space complexity: `O(n)`
where `n` is the length of `nums`

``` python
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        
        indices = deque([]) # monotonic decreasing (but indices)
        
        ans = []
        
        for i in range(n):
            
            if indices and indices[0] <= i-k:   # out of the curr sliding window
                indices.popleft()
            
            while indices and nums[indices[-1]] <= nums[i]:
                indices.pop()
            
            indices.append(i)
            
            ans.append(nums[indices[0]])
        
        return ans[k-1:]
```
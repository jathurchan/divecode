---
date: 2022.11.15
title: 1248. Count Number of Nice Subarrays
difficulty:
    - medium
runtime: 39.98 # faster than (in %)
memory usage: 6.75    # less than (in %)
---
## Description
Given an array of integers `nums` and an integer `k`. A continuous subarray is called **nice** if there are `k` odd numbers on it.

Return *the number of **nice** sub-arrays*.

**Example 1:**

```
Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

```

**Example 2:**

```
Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There is no odd numbers in the array.

```

**Example 3:**

```
Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16

```

**Constraints:**

- `1 <= nums.length <= 50000`
- `1 <= nums[i] <= 10^5`
- `1 <= k <= nums.length`

## Approach 1: Count number of subarrays with an exact constraing
Time complexity: `O(n)`    |    Space complexity: `O(n)`
where `n` is the length of `nums`

``` python
from collections import defaultdict
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        curr = ans = 0
        
        for num in nums:
            curr += (num % 2)   # count only odd numbers
            ans += counts[curr-k]
            counts[curr] += 1
        
        return ans
```
---
date: 2023.02.13
title: 1523. Count Odd Numbers in an Interval Range
difficulty:
    - easy
runtime: 50.4 # faster than (in %)
memory usage: 40.97    # less than (in %)
---
## Description
Given two non-negative integers `low` and `high`. Return the *count of odd numbers between* `low` *and* `high` *(inclusive)*.

**Example 1:**

**Input:** low = 3, high = 7

**Output:** 3

**Explanation:** The odd numbers between 3 and 7 are [3,5,7].

**Example 2:**

**Input:** low = 8, high = 10

**Output:** 1

**Explanation:** The odd numbers between 8 and 10 are [9].

**Constraints:**


- `0 <= low <= high <= 10^9`


## Approach 1: Recursive
Time complexity: `O(1)`    |    Space complexity: `O(1)`


``` python
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low == high:
            return low % 2  # 1 if low is odd, 0 else
        if low % 2 == 1:
            return 1 + self.countOdds(low+1, high)
        if high % 2 == 1:
            return 1 + self.countOdds(low, high-1)
        return (high-low) // 2
```
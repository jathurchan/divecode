---
date: 2022.12.12
title: 70. Climbing Stairs
difficulty:
    - easy
runtime: 71.45 # faster than (in %)
memory usage: 58.8    # less than (in %)
---
## Description
You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

**Example 1:**

```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

```

**Example 2:**

```
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

```

**Constraints:**

- `1 <= n <= 45`

## Approach 1: Dynamic Programming
Time complexity: `O(n)`    |    Space complexity: `O(1)`
where 'n' is the number of steps.

``` python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        curr, prev = 2, 1

        for _ in range(3, n+1):
            curr, prev = prev+curr, curr
        
        return curr
```
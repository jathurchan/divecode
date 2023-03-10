---
date: 2022.11.16
title: 739. Daily Temperatures
difficulty:
    - medium
runtime: 98.93 # faster than (in %)
memory usage: 72.43    # less than (in %)
---
## Description
Given an array of integers `temperatures` represents the daily temperatures, return *an array* `answer` *such that*`answer[i]` *is the number of days you have to wait after the* `ith` *day to get a warmer temperature*. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

**Example 1:**

```
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

```

**Example 2:**

```
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

```

**Example 3:**

```
Input: temperatures = [30,60,90]
Output: [1,1,0]

```

**Constraints:**

- `1 <= temperatures.length <= 105`
- `30 <= temperatures[i] <= 100`

## Approach 1: Monotonic decreasing stack
Time complexity: `O(n)`    |    Space complexity: `O(n)`
where `n` is the length of `temperatures`

``` python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        
        stack = []  # monotonous decreasing
        
        ans = [0] * n
        
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)
        
        return ans
```
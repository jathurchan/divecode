---
date: 2023.01.30
title: 1137. N-th Tribonacci Number
difficulty:
    - easy
runtime: 95.87 # faster than (in %)
memory usage: 60.55    # less than (in %)
languages:
    - python
---
## Description


## Approach 1: Recursion with memoization
Time complexity: `O(n)`    |    Space complexity: `O(n)`


``` python
class Solution:
    def tribonacci(self, n: int) -> int:
        mem = {}
        def getVal(n):
            if n < 2:
                return n
            if n == 2:
                return 1
            if n in mem:
                return mem[n]
            
            mem[n] = getVal(n-3) + getVal(n-2) + getVal(n-1)

            return mem[n]
        
        return getVal(n)
```
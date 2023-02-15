---
date: 2023.02.15
title: 989. Add to Array-Form of Integer
difficulty:
    - easy
runtime: 97.58 # faster than (in %)
memory usage: 85.98    # less than (in %)
---
## Description
The **array-form** of an integer `num` is an array representing its digits in left to right order.


- For example, for `num = 1321`, the array form is `[1,3,2,1]`.

Given `num`, the **array-form** of an integer, and an integer `k`, return *the **array-form** of the integer* `num + k`.

**Example 1:**

**Input:** num = [1,2,0,0], k = 34

**Output:** [1,2,3,4]

**Explanation:** 1200 + 34 = 1234

**Example 2:**

**Input:** num = [2,7,4], k = 181

**Output:** [4,5,5]

**Explanation:** 274 + 181 = 455

**Example 3:**

**Input:** num = [2,1,5], k = 806

**Output:** [1,0,2,1]

**Explanation:** 215 + 806 = 1021

**Constraints:**


- `1 <= num.length <= 104`
- `0 <= num[i] <= 9`
- `num` does not contain any leading zeros except for the zero itself.
- `1 <= k <= 104`


## Approach 1: Iterative


``` python
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        idx = len(num)-1
        num[idx] += k
        while idx > 0 and num[idx] >= 10:
            num[idx-1] = num[idx-1] + num[idx] // 10
            num[idx] = num[idx] % 10
            idx -= 1
        
        while idx == 0 and num[idx] >= 10:
            temp = num[0] // 10
            num[0] = num[0] % 10
            num = [temp] + num
        
        return num
```
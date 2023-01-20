---
date: 2023.01.20
title: 491. Non-decreasing Subsequences
difficulty:
    - medium
runtime: 88.59 # faster than (in %)
memory usage: 85.78    # less than (in %)
---
## Description
Given an integer array `nums`, return *all the different possible non-decreasing subsequences of the given array with at least two elements*. You may return the answer in **any order**.

**Example 1:**

```
Input: nums = [4,6,7,7]
Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]

```

**Example 2:**

```
Input: nums = [4,4,3,2,1]
Output: [[4,4]]

```

**Constraints:**

- `1 <= nums.length <= 15`
- `100 <= nums[i] <= 100`

## Approach 1: Backtracking
Time complexity: `O(n*2^n)`    |    Space complexity: `O(n*2^n)`
where `n` is the length of the input array.

``` python
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr, i):

            if i > len(nums):
                return
            
            if len(curr) > 1 :
                self.ans.append(curr[:])

            seen = set()
            for j in range(i, len(nums)):
                if nums[j] not in seen:
                    if len(curr) == 0 or nums[j] >= curr[-1]:
                        seen.add(nums[j])
                        curr.append(nums[j])
                        backtrack(curr, j+1)
                        curr.pop()

        self.ans = []
        backtrack([], 0)
        return self.ans
```
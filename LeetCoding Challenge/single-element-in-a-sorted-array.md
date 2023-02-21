---
date: 2023.02.21
title: 540. Single Element in a Sorted Array
difficulty:
    - medium
runtime: 15.30 # faster than (in %)
memory usage: 99.62    # less than (in %)
---
## Description
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return *the single element that appears only once*.

Your solution must run in `O(log n)` time and `O(1)` space.

**Example 1:**

**Input:** nums = [1,1,2,3,3,4,4,8,8]

**Output:** 2

**Example 2:**

**Input:** nums = [3,3,7,7,10,11,11]

**Output:** 10

**Constraints:**


- `1 <= nums.length <= 105`
- `0 <= nums[i] <= 105`


## Approach 1: Binary Search
Time complexity: `O(log(n))`    |    Space complexity: `O(1)`


``` python
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1

        while left < right:
            mid = (left + right) // 2

            if mid < len(nums)-1 and nums[mid+1] == nums[mid]:  # single element on the left side
                if mid % 2 == 0:    # number of values on the left side
                    left = mid+2
                else:
                    right = mid-2
            elif mid > 0 and nums[mid-1] == nums[mid]:  # on the right side
                if (mid-1) % 2 == 0: # number of the values on the left side
                    left = mid+1
                else:
                    right = mid-2
            else:
                return nums[mid]
        
        return nums[left]
```
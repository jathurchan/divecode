---
date: 2022.11.14
title: 977. Squares of a Sorted Array
difficulty:
    - easy
runtime: 60.45 # faster than (in %)
memory usage: 49.37    # less than (in %)
---
## Description
Given an integer array `nums` sorted in **non-decreasing** order, return *an array of **the squares of each number** sorted in non-decreasing order*.

**Example 1:**

```
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

```

**Example 2:**

```
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

```

**Constraints:**

- `1 <= nums.length <= 104`
- `104 <= nums[i] <= 104`
- `nums` is sorted in **non-decreasing** order.

**Follow up:**

Squaring each element and sorting the new array is very trivial, could you find an

```
O(n)
```

solution using a different approach?

## Approach 1: Sort
Time complexity: `O(nlog(n))`    |    Space complexity: `O(n)`
where n is the length of `nums`

``` python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([n*n for n in nums])
```


## Approach 2: Two pointers
Time complexity: `O(n)`    |    Space complexity: `O(n)`
where n is the length of `nums`

``` python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = [num*num for num in nums]
        n = len(nums)
        i, j = 0, n-1
        
        result = []
        while i <= j:
            if squares[i] >= squares[j]:
                result.append(squares[i])
                i += 1
            else:
                result.append(squares[j])
                j -= 1
        
        return result[::-1]
```